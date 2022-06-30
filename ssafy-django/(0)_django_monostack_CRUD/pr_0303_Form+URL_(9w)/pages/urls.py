from django.urls import path
from . import views


app_name = 'pages'
urlpatterns = [
    # ~/pages/index/
    path('index/', views.index, name='index')
]
