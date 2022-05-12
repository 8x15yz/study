from .models import TextMessage
from .form import TextMessageForm
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from . import wc
def homepage(request):
    textMessage = TextMessage.objects.order_by('-pk')
    
    total_text=''
    for i in range(len(textMessage)):
        total_text += textMessage[i].content
    
    wc.tm(total_text)
    context={
        
    }
    return render(request,'thpr/homepage.html',context)

    

def index(request):
    texts = TextMessage.objects.order_by('-pk')
    context = {
        'texts':texts
    }
    return render(request, 'thpr/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        textMessage = TextMessageForm(request.POST)
        if textMessage.is_valid():
            textMessage.save()
            
            return redirect('thpr:index')
    else:
        textMessage = TextMessageForm()
    context = {
        'textMessage': textMessage,
    }
    return render(request, 'thpr/create.html', context)




    