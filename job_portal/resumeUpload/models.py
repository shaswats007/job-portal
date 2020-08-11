from django.db import models
#from .models import File
# Create your models here.

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name