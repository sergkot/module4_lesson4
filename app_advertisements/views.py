from django.shortcuts import render
from .models import Advertisements
from django.http import HttpResponse
import glob
import os


def index(request):
    # return HttpResponse('Успешно')
    advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    # return HttpResponse('Успешно')
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    # return HttpResponse('Успешно')
    return render(request, 'advertisement-post.html')

def register(request):
    # return HttpResponse('Успешно')
    return render(request, 'register.html')

def login(request):
    # return HttpResponse('Успешно')
    return render(request, 'login.html')

def profile(request):
    # return HttpResponse('Успешно')
    return render(request, 'profile.html')


def test_page(request):
    return render(request, 'test_page_static.html')
    # mylist = [f for f in glob.glob("*.*")]
    # return render(request, 'test_page_static.html')
    # mylist = [f for f in glob.glob("*.*")]
    # print(mylist)
    #
    # return HttpResponse('files: ' + str(mylist))

    # file_location = 'test_page.html'
    # with open(file_location, 'r') as f:
    #     file_data = f.read()
    # print(file_data)
    # return HttpResponse(file_data, content_type='html')
# Create your views here.
