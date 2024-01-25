from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Data is inserted into  topic model form')

    return render(request,'insert_topic.html',context=d)

def insert_webpage(request):
    EFWO=WebpageForm()
    d={'EFWO':EFWO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Data inserted into webpage model form')

    return render(request,'insert_webpage.html',context=d)


def insert_accessrecord(request):
    EFAO=AccessRecordForm()
    d={'EFAO':EFAO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('Data is inserted into accessrecord model form')

    return render(request,'insert_accessrecord.html',context=d)

