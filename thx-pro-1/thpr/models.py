from pyexpat import model
from django.db import models
from django.conf import settings
# Create your models here.
class TextMessage(models.Model):
    
    title = models.CharField(max_length=20)
    content = models.TextField()
    autor = models.CharField(max_length=10)
    