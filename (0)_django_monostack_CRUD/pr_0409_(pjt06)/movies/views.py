from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm


def index(request):
    movies = Movie.objects.order_by('-pk')

    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movies':movies,
    }
    return render(request, 'movies/detail.html', context)

def update(request, movie_pk):
    if request.method == 'POST':
        movies = get_object_or_404(Movie, pk=movie_pk)
        form = MovieForm(request.POST, request.FILES, instance=movies)

        if form.is_valid():
            movies = form.save()
            return redirect('movies:detail', movies.pk)
    else:
        movies = get_object_or_404(Movie, pk=movie_pk)
        form = MovieForm(instance=movies)
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)


def delete(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movies.delete()
        return redirect('movies:index')
    return redirect('movies:detail', movies.pk)

