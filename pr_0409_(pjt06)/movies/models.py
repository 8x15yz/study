from email.mime import image
from hashlib import blake2b
from pyexpat import model
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)         # 영화 제목
    audiance = models.IntegerField(null=True)       # 관객 수
    release_date = models.DateField(auto_now=False) # 개봉일
    genre = models.CharField(max_length=30)         # 장르
    score = models.FloatField(null=True)            # 평점
    poster_url = models.TextField()                 # 포스터 경로
    description = models.TextField()                # 줄거리
    
    # 추가 작업 => 이미지를 사용자에게서 받아와 게시하는 기능
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.pk} - {self.title} - {self.audiance} - {self.release_date} - {self.genre} - {self.score} - {self.poster_url} - {self.description}'
