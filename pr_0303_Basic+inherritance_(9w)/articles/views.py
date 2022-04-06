from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')

def variable(request):
    foods = ['족발', '스무디', '베개', '시계']
    pick = random.choice(foods)
    context = {
        'pick':pick,
    }
    return render(request, 'variable.html', context)

def dinner(request):
    foods = ['코코넛', '스무디', '이불', '아이스크림']
    pick = random.choice(foods)
    context = {
        'pick':pick,
        'foods':foods,
    }
    return render(request, 'dinner.html', context)

def Tags(request):
    foods = ['코코넛', '스무디', '이불', '아이스크림']
    pick = random.choice(foods)
    context = {
        'pick':pick,
        'foods':foods,
    }
    return render(request, 'Tags.html', context)

def comments(request):
    return render(request, 'comments.html')

