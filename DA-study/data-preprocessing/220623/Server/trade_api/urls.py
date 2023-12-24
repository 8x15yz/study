from django.urls import path
from . import views

urlpatterns = [
    path('trade_list', views.trade_list)
]
