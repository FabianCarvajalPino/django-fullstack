#from __future__ import unicode_literals
from django.db import models


# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['title']) < 2:
            errors['title'] = "El titulo deberia tener al menos 2 caracteres"
        if len(postData['network']) < 3:
            errors['network'] = "El network debe tener al menos 3 caracteres"
        
        if len(postData['description']) < 10:
            errors['desc'] = "La descripción debe tener al menos 10 caracteres"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()