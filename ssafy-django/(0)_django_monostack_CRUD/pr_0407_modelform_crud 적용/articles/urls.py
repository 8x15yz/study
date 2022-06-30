from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # GET 방식으로 조회를 하는 것이고 게시물 페이지를 렌더한다
    path('', views.index, name = 'index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]

