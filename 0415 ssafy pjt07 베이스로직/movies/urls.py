from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:m_pk>/', views.detail, name="detail"),
    path('<int:m_pk>/update/', views.update, name='update'),
    path('<int:m_pk>/delete/', views.delete, name='delete'),
    path('<int:m_pk>/delete/', views.delete, name='delete'),

    # 댓글 로직
    path('<int:m_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:m_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),

]