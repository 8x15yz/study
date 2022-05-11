from .models import TextMessage
from .form import TextMessageForm
from django.shortcuts import render


def index(request):
    datum = TextMessage.objects.all()
    context = {
        'datum':datum
    }
    return render(request, 'thpr.index.html', context)


def create(request):
    form = TextMessageForm()
    context = {
        'form':form
    }
    return render(request, 'thpr.index.html', context)


def detail(request, pk):
    data = TextMessage.objects.get(pk=pk)
    return 
    