from django.shortcuts import redirect, render, get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, m_pk):
    movie = get_object_or_404(Movie, pk=m_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie':movie,
        'comment_form': comment_form,
        'comments':comments,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def update(request, m_pk):
    movie = get_object_or_404(Movie, pk=m_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            
            form = MovieForm(request.POST, instance=movie)

            if form.is_valid():
                movie = form.save()
                return redirect('movies:detail', m_pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')
    context = {
        'movie':movie,
        'form':form,
    }
    return render(request, 'movies/create.html', context)


@require_POST
def delete(request, m_pk):
    movie = get_object_or_404(Movie, pk=m_pk)
    if request.user.is_authenticated:
        if request.user == movie.user:
            movie.delete()
    return redirect('movies:index')


def comments_create(request, m_pk):
    movie = Movie.objects.get(pk=m_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
    return redirect('movies:detail', movie.pk)
    
def comments_delete(request, m_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', m_pk)