from django.db import models


class Directory(models.Model):
    name = models.CharField(max_length=50)
    fullpath = models.CharField(max_length=200)
