from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles
    }
    


    return render(request, 'articles/index.html', context)

#throw
def new(request):
    return render(request, 'articles/new.html')

#catch
def create(request):

    title = request.POST.get('title')
    content = request.POST.get('content')

    # create 사용하기
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # return render(request, 'articles/create.html')
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk) 
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article_pk)