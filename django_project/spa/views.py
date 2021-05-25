from django.http import HttpResponse
from django.shortcuts import render
from .models import Service
from  .models import Master

def homepage(request):
    return HttpResponse('Сайт')

def services(request):
    services = Service.objects.all()
    return render(request,'service.html',{'services':services})

def masters(request):
    masters = Master.objects.all()
    return render(request,'master.html',{'masters':masters})