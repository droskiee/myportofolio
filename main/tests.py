from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from main.models import Experience, Skill


# ==================== TEST UI & MODEL LAMA ====================

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time"
        )
        self.skill = Skill.objects.create(
            name="Python",
            category="language",
            proficiency_level=90
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_skills")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="experienceContainer"')
        self.assertContains(response, 'id="searchInput"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="experienceContainer"')

        # Menguji endpoint API list
        api_response = self.client.get(reverse("api:experience-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        self.assertFalse(self.experience.is_ongoing)

        # Menguji endpoint API list setelah experience selesai
        response = self.client.get(reverse("api:experience-list"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]["ended_at"])

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Python")
        self.assertEqual(self.skill.category, "language")
        self.assertEqual(self.skill.proficiency_level, 90)

    def test_skills_page(self):
        response = self.client.get(reverse("main:show_skills"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")
        self.assertContains(response, self.skill.name)
        self.assertContains(response, "90")

    def test_empty_skills_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skills"))
        self.assertContains(response, "Belum ada data skill yang ditambahkan.")


# ==================== TEST DRF API TUGAS 6 ====================

class ExperienceAPITestCase(APITestCase):
    def setUp(self):
        # 1. Setup Klien & Pengguna 4 Role
        self.anonymous_client = APIClient()

        self.regular_user = User.objects.create_user(username="regular", password="password123")
        self.editor_user = User.objects.create_user(username="editor", password="password123")
        
        # Tambahkan editor ke Group 'Editor'
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        self.editor_user.groups.add(editor_group)

        self.superuser = User.objects.create_superuser(username="admin", password="password123")

        # 2. Sample Data Experience
        self.exp = Experience.objects.create(
            title="Software Engineer Intern",
            description="Developing web services",
            category="internship"
        )

        # 3. URL Resolvers
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", kwargs={"pk": self.exp.id})
        self.star_url = reverse("api:experience-star", kwargs={"pk": self.exp.id})

    # Test GET List & Search dapat diakses Pengunjung tanpa login
    def test_get_experiences_and_search_allowed_for_everyone(self):
        response = self.anonymous_client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Search Query Param ?q=
        search_response = self.anonymous_client.get(f"{self.list_url}?q=Intern")
        self.assertEqual(search_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(search_response.json()), 1)

    # Test Penolakan POST/DELETE Pengunjung & Pengguna Biasa + Verifikasi DB
    def test_anonymous_and_regular_user_cannot_create_or_delete(self):
        payload = {"title": "New Exp", "description": "Desc", "category": "full-time"}
        initial_count = Experience.objects.count()

        # Penolakan POST Pengunjung
        response = self.anonymous_client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), initial_count)  # Verifikasi DB

        # Penolakan POST Pengguna Biasa
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), initial_count)  # Verifikasi DB

        # Penolakan DELETE Pengguna Biasa
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Experience.objects.filter(pk=self.exp.id).exists())  # Verifikasi DB

    # Test Hak Akses Editor (PATCH diizinkan, POST & DELETE ditolak + Verifikasi DB)
    def test_editor_can_patch_but_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor_user)
        initial_count = Experience.objects.count()

        # Editor PATCH (Berhasil)
        response = self.client.patch(self.detail_url, {"title": "Updated by Editor"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.exp.refresh_from_db()
        self.assertEqual(self.exp.title, "Updated by Editor")

        # Editor POST (Ditolak)
        payload = {"title": "New Exp", "description": "Desc", "category": "full-time"}
        response = self.client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), initial_count)  # Verifikasi DB

        # Editor DELETE (Ditolak)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Experience.objects.filter(pk=self.exp.id).exists())  # Verifikasi DB

    # Test Hak Akses Pemilik Portofolio / Superuser (Akses Full POST & DELETE)
    def test_superuser_can_create_and_delete(self):
        self.client.force_authenticate(user=self.superuser)

        # Superuser POST (Berhasil)
        payload = {"title": "Superuser Exp", "description": "Desc", "category": "full-time"}
        response = self.client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Experience.objects.count(), 2)

        # Superuser DELETE (Berhasil)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Experience.objects.filter(pk=self.exp.id).exists())

    # Test Fitur Star (Pengunjung Ditolak, User Authenticated Diizinkan)
    def test_star_feature_permissions(self):
        # Pengunjung Star (Ditolak)
        response = self.anonymous_client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.exp.stars.count(), 0)

        # User Authenticated Star (Berhasil Toggle)
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.exp.stars.count(), 1)
        self.assertTrue(response.json()["is_starred"])

    # Test Validasi Input Text (strip_tags di Serializer)
    def test_input_validation_strip_tags(self):
        self.client.force_authenticate(user=self.superuser)
        payload = {
            "title": "<b>Backend Dev</b>",
            "description": "<script>alert('xss')</script>Pengalaman kerja",
            "category": "full-time"
        }
        response = self.client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_exp = Experience.objects.get(id=response.json()["id"])
        self.assertEqual(created_exp.title, "Backend Dev")
        self.assertNotIn("<b>", created_exp.title)
        self.assertNotIn("<script>", created_exp.description)

    # Test Penolakan Request Mutasi tanpa CSRF Token
    def test_csrf_protection_enforced(self):
        csrf_client = APIClient(enforce_csrf_checks=True)
        login_success = csrf_client.login(username="admin", password="password123")
        self.assertTrue(login_success)

        payload = {"title": "CSRF Test", "description": "Test Desc", "category": "full-time"}
        # Request POST tanpa header X-CSRFToken wajib ditolak (403)
        response = csrf_client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)