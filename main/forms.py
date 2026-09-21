from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput
from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Posisi / Peran",
            "description": "Deskripsi Pekerjaan",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Thumbnail / Logo",
            "ended_at": "Tanggal Selesai (Opsional)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineer Intern",
                    "maxlength": 255,
                    "class": "form-control",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan tanggung jawab atau kegiatanmu...",
                    "rows": 3,
                    "class": "form-control",
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                    "class": "form-control",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                }
            ),
        }