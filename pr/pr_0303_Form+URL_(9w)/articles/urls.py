from django.urls import path
from . import views

# URL Namespace
app_name = 'articles'
urlpatterns = [
    # ~/articles/index/ => (views의 index 함수랑 연결) => index 페이지를 보여주도록
    path('index/', views.index, name='index'),

    # ~/articles/throw/ => views의 throw 함수랑 연결
    path('throw/', views.throw, name='throw'),

    # ~/articles/catch/ => views의 catch 함수랑 연결
    path('catch/', views.catch, name='catch'),

    # ~/articles/hello/사람이름(글자)/
    path('hello/<name>/', views.hello, name='hello'),

    # ~/articles/number/숫자/
    path('number/<int:pk>/', views.number, name='number'),
]
