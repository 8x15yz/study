from pyexpat import model
from django.db import models

# Create your models here.
class TextMessage(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()