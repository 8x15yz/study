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
    <title>Document</title>
    
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{% url 'articles:index' %}">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" href="{% url 'articles:new' %}">새 글 쓰기</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled">Disabled</a>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
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

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    creates_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.pk} - {self.title} - {self.content}'
```



## urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),

    path('new/', views.new, name='new'), 

    path('create/', views.create, name='create'),

    path('<int:article_pk>/setail/', views.detail, name='detail'),

    path('<int:article_pk>/delete/', views.delete, name='delete'),

    path('<int:article_pk>/edit/',  views.edit, name='edit'),

    path('<int:article_pk>/update/', views.update, name='update'),

]
```



## views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
```

```python
def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
```

```python
#throw
def new(request):
    return render(request, 'articles/new.html')
```

```python
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
```

```python
def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk) 
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

```python
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')
```

```python
def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)
```

```python
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article_pk)
```



## templates/articles/

### create.html

```html
{% extends 'base.html' %}

{% block content %}
작성완료햇습니다 !!
{% endblock content %}
```



### detail.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>상세 페잊지</h1>
<div class="col-8">
    <div class="card">
        <div class="card-body">
            <p>{{article.pk}}</p>
            <p>{{article.title}}</p>
            <p>{{article.content}}</p>
            <p>{{article.creates_at}}</p>
            <p>{{article.updated_at}}</p>
            <a href="{% url 'articles:edit' article.pk%}" class="btn btn-success">수정하기</a>
            <a href="{% url 'articles:delete' article.pk%}" class="btn btn-danger">삭제하기</a>
        </div>
    </div>
</div>
{% endblock content %}
```



### edit.html

```html
{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">글 수정하기</h1>

<form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    
    <div class="row justify-content-center">
        <div class="col-6">
            <div class="mb-3">
                <label for="title" class="form-label">제목</label>
                <input type="text" name="title" id="title" class="form-control" value="{{article.title}}">
            </div>
            
            <div class="mb-3" class="form-label">
                <label for="">내용</label>
                <textarea name="content" id="content" cols="30" rows="10" class="form-control">{{article.content}}</textarea>
            </div>
            
            <button class="btn btn-primary">submit</button>
        </div>
    </div>
</form>

{% endblock content %}
```



### index.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>index</h1>

{% comment %} {% for article in articles %}
<p>
    {{article}}
</p>

{% endfor %} {% endcomment %}

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4">
    {% for article in articles %}
      <div class="col">
        <div class="card">
          <a href="{% url 'articles:detail' article.pk%}">
            <img src="https://picsum.photos/500" class="card-img-top" alt="예시 이미지">
            <div class="card-body">
            <h5 class="card-title">{{article.pk}}. {{article.title}}</h5>
            <p class="card-text">{{article.content}}</p>
            </div>
          </a>
          
        </div>
      </div>
    {% endfor %}    
</div>

{% endblock content %}
```



### new.html

```html
{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">새 글 작성</h1>

<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    
    <div class="row justify-content-center">
        <div class="col-6">
            <div class="mb-3">
                <label for="title" class="form-label">제목</label>
                <input type="text" name="title" id="title" class="form-control">
            </div>
            
            <div class="mb-3" class="form-label">
                <label for="">내용</label>
                <textarea name="content" id="content" cols="30" rows="10" class="form-control"></textarea>
            </div>
            
            <button class="btn btn-primary">submit</button>
        </div>
    </div>
</form>
{% endblock content %}
```



