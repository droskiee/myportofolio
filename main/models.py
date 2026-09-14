import uuid
from django.db import models

# Model Experience kamu yang sudah ada:
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None


# Tambahkan model Skill di bawahnya:
class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework & Library'),
        ('tools', 'Tools & Technologies'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)                    # Field 1
    category = models.CharField(max_length=50, choices=SKILL_CATEGORIES, default='language')  # Field 2
    proficiency_level = models.IntegerField()                  # Field 3 (cth: 1-100 atau level persentase)
    description = models.TextField(blank=True, null=True)      # Field tambahan (opsional)

    def __str__(self):
        return self.name