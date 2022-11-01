from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='project/images/')
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
