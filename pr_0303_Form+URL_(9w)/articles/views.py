from django.shortcuts import render


# 1. 첫번째 파라미터 : request
def index(request):
    """HTML 랜더 (index page)"""
    # templates 이름!! (s 주의!!)
    return render(request, 'articles/index.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # request : 현재 요청 모든 정보
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'articles/catch.html', context)


# 2번째 파라미터 부터 variable routing
def hello(request, name):
    print(type(name))
    context = {
        'name': name
    }
    return render(request, 'articles/hello.html', context)


def number(request, pk):
    print(type(pk))
    context = {
        'pk': pk
    }
    return render(request, 'articles/number.html', context)
