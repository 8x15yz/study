from django.urls import path
from . import views

app_name = 'thpr'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('detail/', views.detail, name="detail"),
    # path('delete/<int:pk>/', views.delete, name="delete")
]