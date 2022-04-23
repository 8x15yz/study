# from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from articles.models import (
    Article,
    Comment,
)
from articles.serializers import (
    ArticleListSerializer,
    ArticleCreateSerializer,
    ArticleDetailSerializer,
    CommentListSerializer,
    CommentCreateSerializer,
)


@api_view(['GET', 'POST'])
def list_create(request):
    if request.method == 'GET':
        # articles => query set & article => instance
        articles = Article.objects.order_by('-pk')
        # serializer로 변환!
        serializer = ArticleListSerializer(articles, many=True)
        # data 형태
        return Response(serializer.data)
    elif request.method == 'POST':
        # request.POST & request.GET
        # => request.data
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 넘겨준 정보가 잘 저장이 되었다!
            return Response(serializer.data, HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_update_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response({'message': f'{pk}번 게시글이 삭제 되었습니다.'}, HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def comment_list_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        comments = get_list_or_404(article.comment_set.order_by('-pk'))
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, article_pk, pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(article.comment_set, pk=pk)
    if request.method == 'PUT':
        serializer = CommentCreateSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message': f'{pk}번 댓글이 삭제되었습니다.'}, HTTP_204_NO_CONTENT)
