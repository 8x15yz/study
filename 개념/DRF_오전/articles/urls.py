from django.urls import path
from . import views


urlpatterns = [
    # GET ~/api/v1/articles/
    # POST
    path('', views.article_list_create),
    # GET ~/api/v1/articles/:pk/
    # PUT
    # DELETE
    path('<int:pk>/', views.article_detail_update_delete),

    # GET ~/api/v1/articles/:pk/comments/
    # POST pk번째 게시글의 댓글을 추가
    path('<int:pk>/comments/', views.article_comment_list_create),

    # UPDATE ~/api/v1/articles/:article_pk/comments/:pk/
    # DELETE 수정 / 삭제
    path('<int:article_pk>/comments/<int:pk>/', views.article_comment_update_delete),
]