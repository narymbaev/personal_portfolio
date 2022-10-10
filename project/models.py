from distutils.command.upload import upload
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project/images')

    def __str__(self) -> str:
        return self.title
