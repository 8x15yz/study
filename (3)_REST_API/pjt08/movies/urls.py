from django.urls import path
from . import views

urlpatterns = [
    # 배우정보 전체조회
    path('actors/', views.actor_list),

    # 배우 상세정보 조회
    path('actors/<int:pk>/', views.actor_detail),

    # 영화정보 전체조회
    path('movies/', views.movie_list),

    # 영화 상세정보 조회
    path('movies/<int:pk>/', views.movie_detail),
        
    # 리뷰 작성
    path('movies/<int:pk>/reviews/', views.create_review),
        
    # 리뷰 전체리스트 조회
    path('reviews/', views.review_list),
        
    # 리뷰 개별데이터 조회 + 리뷰 수정 + 리뷰 삭제
    path('reviews/<int:pk>/', views.review_detail),

]