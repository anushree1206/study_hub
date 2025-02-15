from django.contrib import admin
from .models import StudyMaterial
# Register your models here.
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.register(StudyMaterial)
