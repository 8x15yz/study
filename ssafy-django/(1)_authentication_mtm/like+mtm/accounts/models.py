from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # 유저가 팔로우하는 사람들 
    # 해당 유저를 팔로우하는 사람들을 키워드를 구분해서 만듦
    # 


