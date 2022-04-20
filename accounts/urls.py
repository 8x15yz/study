from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('userindex/', views.userindex, name='userindex'),
    path('<username>/', views.profile, name='profile'),
]