from django.urls import path
from .views import articles, comments


urlpatterns = [
    # GET ~/api/v1/articles/
    # POST
    path('articles/', articles.list_create),
    # GET ~/api/v1/articles/:pk/
    # PUT
    # DELETE
    path('articles/<int:pk>/', articles.detail_update_delete),

    # GET ~/api/v1/articles/:pk/comments/
    # POST pk번째 게시글의 댓글을 추가
    path('articles/<int:pk>/comments/', articles.comment_list_create),

    # UPDATE ~/api/v1/articles/:article_pk/comments/:pk/
    # DELETE 수정 / 삭제
    path('articles/<int:article_pk>/comments/<int:pk>/', articles.comment_update_delete),

    # =================
    path('comments/<int:pk>/', comments.update_delete),
]