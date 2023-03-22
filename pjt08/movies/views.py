from .models import (
    Actor,
    Movie,
    Review,
)
from .serializers import (
    ActorListSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieSerializer,
    ReviewListSerializer,
    ReviewSerializer,
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from django.shortcuts import get_object_or_404, get_list_or_404



@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.order_by('-pk')
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, pk):
    if request.method == 'GET':
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-pk')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
def create_review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, HTTP_201_CREATED)

@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.order_by('-pk')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response({'message': f'{pk}번 리뷰를 삭제했습니다'}, HTTP_204_NO_CONTENT)