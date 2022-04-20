from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('userindex/', views.userindex, name='userindex'),
    path('signup/', views.signup, name='signup'),
    path('<username>/', views.profile, name='profile'),
]