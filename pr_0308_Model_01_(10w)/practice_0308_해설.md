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

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.pk}. 제목: {self.title} - 내용: {self.content}'
```



## urls.py

```python
from django.urls import path
from . import views

# URL namespace
app_name = 'articles'

urlpatterns = [
    # ~/articles/
    path('', views.index, name='index'),

    # ~/articles/new/ => 새 글 쓰기 페이지 랜더
    path('new/', views.new, name='new'),

    # ~/articles/create/ => 입력받은 정보 DB에 적용
    path('create/', views.create, name='create'),

    # ~/articles/10/ => 상세 페이지 렌더 (ex. pk가 10인 상세페이지)
    path('<int:article_pk>/', views.detail, name='detail'),

    # Update & Delete 목요일에!!
]
```



## views.py

```python
from django.shortcuts import render, redirect
from .models import Article
```

```python
def index(request):
    """index 페이지 랜더"""
    # Database에서 articles 전체 조회 (Read)
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }

    # Template namespace
    return render(request, 'articles/index.html', context)
```

```python
# throw
def new(request):
    """새 글 쓰기 페이지 랜더"""
    return render(request, 'articles/new.html')
```

```python
# catch
def create(request):
    """입력 받은 정보 DB에 추가(Create)"""
    # ex) ?title=제목입니다&content=내용입니다
    # => Method GET => request.GET 주머니
    # title = request.GET.get('title') # title 꺼내 쓰고
    # content = request.GET.get('content') # content 꺼내 쓴다

    # Method POST
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1
    # # Article Model Class => Instance
    # article = Article()
    # # 인스턴스에 속성 저장
    # article.title = title
    # article.content = content
    # # SAVE
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()

    # 3
    # article = Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html') # create.html은 필요 X
    # 리디렉션
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

```python
def detail(request, article_pk):
    """article_pk에 해당하는 상세 페이지 랜더"""
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```



## templates/articles/

### detail.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>상세 페이지</h1>
<p>{{ article.pk }}</p>
<p>{{ article.title }}</p>
<p>{{ article.content }}</p>
<p>{{ article.created_at }}</p>
<p>{{ article.updated_at }}</p>
{% endblock content %}
```

### index.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>Index</h1>

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4">
  {% for article in articles %}
    <div class="col">
      <div class="card">
        <a href="{% url 'articles:detail' article.pk %}">
          <img src="https://picsum.photos/500" class="card-img-top" alt="예시 이미지">
          <div class="card-body">
            <h5 class="card-title">{{ article.pk }}. {{ article.title }}</h5>
            <p class="card-text">{{ article.content }}</p>
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
<h1 class="text-center mt-5">새 글 작성</h1>
{% comment %} url tag 사용하기 {% endcomment %}
{% comment %} '앱이름:유알엘별명' {% endcomment %}
{% comment %} default method : GET {% endcomment %}
<div class="row justify-content-center">
  <div class="col-6">
    <form action="{% url 'articles:create' %}" method="POST">
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
  </div>
</div>
{% endblock content %}
```



