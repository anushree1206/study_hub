from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)

class StudyMaterial(models.Model):
    MATERIAL_TYPES = [
        ('PDF', 'PDF'),
        ('VIDEO', 'Video'),
        ('WEBSITE', 'Website'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    resource_type = models.CharField(max_length=10, choices=MATERIAL_TYPES)
    external_link = models.URLField()

    def __str__(self):
        return self.title