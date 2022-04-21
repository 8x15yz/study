from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('userindex/', views.userindex, name='userindex'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('profile/<str:username>/retrieve/<int:p_pk>/', views.retrieve, name='retrieve'),

    # 댓글로직
    path('profile/<str:username>/retrieve/<int:p_pk>/comments/', views.comments_create, name='comments_create'),

]