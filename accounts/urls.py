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

]