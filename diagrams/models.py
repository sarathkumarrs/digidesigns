from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Module(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)


class Process(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
