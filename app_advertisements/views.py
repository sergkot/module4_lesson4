from django.shortcuts import render
from django.http import HttpResponse
import glob
import os


def index(request):
    return HttpResponse('Успешно')

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
