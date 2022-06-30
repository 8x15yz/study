# practice/

## urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```



## settings.py

```python
INSTALLED_APPS = [
    'articles',
    'django_extensions',
	...
]

...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



# templates/

## base.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  {% block css %}
  {% endblock css %}
  <title>Document</title>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'articles:index' %}">전체 게시글</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'articles:create' %}">새 글 쓰기</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  
  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```



# articles/

## models.py

```python
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.pk}. {self.title}'


# 1. model 변경사항 발생 => (변경사항이 DB에도 반영이 되어야함!)

# 2. migration 파일 준비 : makemigrations

# 3. 준비된 파일로 migrate : migrate

# showmigrations

# sqlmigrate
```



## urls.py

```python
from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    # READ (ALL)
    # ~/articles/
    path('', views.index, name='index'),


    # # CREATE
    # # 1. 게시글 쓸 수 있는 양식(form) 주세요
    # # ~/articles/new/ : GET
    # path('new/', views.new, name='new'), 

    # # 2. 양식(form)을 완성해서 제출 => 생성
    # # ~/articles/create/ : POST
    # path('create/', views.create, name='create'),

    # url 하나로도 가능! GET / POST
    path('create/', views.create, name='create'),


    # READ (detail)
    # ~/articles/게시글pk/
    path('<int:article_pk>/', views.detail, name='detail'),

    # DELETE
    # ~/articles/게시글pk/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),

    # UPDATE
    # 1. 게시글 수정할 수 있는 양식 주세요
    # ~/articles/게시글pk/edit/
    path('<int:article_pk>/edit/', views.edit, name='edit'),

    # 2. 양식을 완성해서 제출 => 수정
    # ~/articles/게시글pk/update/
    path('<int:article_pk>/update/', views.update, name='update')
]
```



## views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
```

```python
def index(request):
    """게시글 전체 조회 페이지 랜더"""
    # 1 ~ N
    # articles = Article.objects.all()
    # articles = Article.objects.all()[::-1]
    # N ~ 1
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
```

```python
# def new(request):
#     """게시글 작성 페이지 랜더"""
#     return render(request, 'articles/new.html')
```

```python
# def create(request):
#     """입력받은 정보를 바탕으로 DB에 데이터 추가"""
#     # 입력받은 정보 준비
#     # request.주머니 : 보내는 방식에 따라 담겨있는 주머니가 다름!
#     # request.GET
#     # request.POST => POST 사용!!

#     # input tag & textarea tag : name attr.
#     title = request.POST.get('title')
#     content = request.POST.get('content')

#     # DB에 데이터 추가
#     article = Article()
#     article.title = title
#     article.content = content
#     article.save()

#     return redirect('articles:index')
```

```python
    """
    GET : 게시글 작성 페이지 랜더
    POST : 입력받은 정보를 바탕으로 DB에 데이터 추가
    """
    if request.method == 'POST':
        # POST를 먼저 작성한 이유 => 나중에!
        # method 방식이 POST
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article.pk)
    else:
        # method 방식이 GET
        return render(request, 'articles/new.html')
```

```python
def detail(request, article_pk):
    """게시글 상세 페이지를 랜더"""
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

```python
def delete(request, article_pk):
    """게시글 DB에서 삭제"""
    if request.method != 'POST':
        return redirect('articles:detail', article_pk)

    # 1. 어떤 게시글?
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    # 2. 삭제
    article.delete()

    return redirect('articles:index')
```

```python
def edit(request, article_pk):
    """게시글 수정 페이지 랜더"""
    # 1. 기존 게시글 정보가 필요하다!
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article
    }
    # 2. 넘겨주기
    return render(request, 'articles/edit.html', context)
```

```python

def update(request, article_pk):
    """입력받은 정보를 바탕으로 DB에 데이터 수정"""
    # 1. 어떤 게시글을 수정할건지?
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    # 2. 변경할 정보
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 3. 인스턴스의 속성 변경
    article.title = title
    article.content = content

    # 4. DB에 반영
    article.save()

    # return redirect('articles:detail', article_pk)
    return redirect('articles:detail', article.pk)
```



## templates/articles/



### detail.html

```html
{% extends 'base.html' %}

{% block content %}
<div class="row">
  <h1>상세 페이지</h1>
  <div class="col-8">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ article.title }}</h5>
        <p class="card-text">{{ article.content }}</p>
        <p>{{ article.created_at }}</p>
        <p>{{ article.updated_at }}</p>
        <a class="btn btn-success" href="{% url 'articles:edit' article.pk %}">수정하기</a>
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#exampleModal">
          삭제하기
        </button>
      </div>
    </div>
  </div>
</div>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">정말로 삭제하시겠습니까?</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        삭제된 정보는 복구가 불가능합니다 :(
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <form action="{% url 'articles:delete' article.pk %}" method="POST">
          {% csrf_token %}
          <button class="btn btn-danger">삭제하기</button>
        </form>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```



### edit.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>글 수정하기</h1>

<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% comment %} POST 방식에서 필수! {% endcomment %}
  {% csrf_token %}
  <div class="mb-3">
    <label for="title" class="form-label">제목</label>
    <input type="text" name="title" id="title" class="form-control" value="{{ article.title }}">
  </div>
  <div class="mb-3">
    <label for="content" class="form-label">내용</label>
    <textarea name="content" id="content" cols="30" rows="10" class="form-control">{{ article.content }}</textarea>
  </div>
  <button class="btn btn-primary">제출</button>
</form>
{% endblock content %}
```



### index.html

```html
{% extends 'base.html' %}

{% block css %}
<style>
  .card:hover {
    background-color: burlywood;
  }
</style>
{% endblock css %}

{% block content %}
<div class="row row-cols-1 row-cols-md-2 g-4">
  {% for article in articles %}
    <div class="col">
      <a href="{% url 'articles:detail' article.pk %}" class="text-decoration-none">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ article.title }}</h5>
            <p class="card-text">{{ article.content }}</p>
          </div>
        </div>
      </a>
    </div>
  {% endfor %}
</div>
{% endblock content %}
```



### new.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>새 글 쓰기</h1>

<form action="{% url 'articles:create' %}" method="POST">
  {% comment %} POST 방식에서 필수! {% endcomment %}
  {% csrf_token %}
  <div class="mb-3">
    <label for="title" class="form-label">제목</label>
    <input type="text" name="title" id="title" class="form-control">
  </div>
  <div class="mb-3">
    <label for="content" class="form-label">내용</label>
    <textarea name="content" id="content" cols="30" rows="10" class="form-control"></textarea>
  </div>
  <button class="btn btn-primary">제출</button>
</form>
{% endblock content %}
```



