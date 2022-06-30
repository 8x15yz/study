from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.order_by('-pk')  # 쿼리셋을 들고옴
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # POST : DB에 새글 추가
    # GET : 새글 쓰기 페이지를 보여준다

    # if 부분은 create 함수 부분
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()  # 인스턴스 안에 pk정보가 있으니까 
            return redirect('articles:detail', article.pk)
        # 
    else: # else부분은 new 함수 부분
        form = ArticleForm() # 인스턴스를 실행홰주는 부분
        # 새글쓰기 페이지를 보여주기 => 폼 인스턴스를 받아올거야
    context = {
        'form':form,
    }
    return render(request, 'articles/update.html', context)

def detail(request, article_pk):
    # 특정 게시물의 상세페이지를 보여준다
    # 조회시도하는 페이지가 없을때 404를 보여준다
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, article_pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article_pk)
    else:
        article = get_object_or_404(Article, pk=article_pk)
        form = ArticleForm(instance=article)
    context = {
        'form':form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

