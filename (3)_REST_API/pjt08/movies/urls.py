from django.urls import path
from . import views

urlpatterns = [
    path('actors/lists/', views.actor_list),
    path('actors/<int:actors_pk>/', views.actor_detail),
    path('movies/lists/', views.movie_list),
    path('movies/<int:movies_pk>/', views.movie_detail),
    path('movies/<int:pk>/reviews/', views.create_review),
    path('reviews/', views.review_list),
    path('reviews/<int:pk>/', views.review_detail),
]