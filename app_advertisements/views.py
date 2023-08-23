from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementsForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
import glob
import os


def index(request):
    # return HttpResponse('Успешно')
    advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements, 'pictures': 'blablabla'}
    return render(request, 'app_advertisements/index.html', context)


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('advertisement-post')
            return redirect(url)
            #########
            # try:
            #     advertisement.save()
            #     url = reverse('main-page')
            #     return redirect(url)
            # except ValueError as ve:
            #     return ve
        else:
            return render(request, 'app_advertisements/advertisement-post.html', {'form': form})
    else:
        # advertisements = Advertisements.objects.all()
        context = {'form': AdvertisementsForm, 'var1': 'variable test'}
        # print(f'cont: {context}')
        return render(request, 'app_advertisements/advertisement-post.html', context)


def top_sellers(request):
    # return HttpResponse('Успешно')
    return render(request, 'app_advertisements/top-sellers.html')


def advertisement(request):
    # return HttpResponse('Успешно')
    id = int(request.GET.get("id", -1))
    if id != -1:
        print(f'id from url {id}')
        for adv in Advertisements.objects.all():
            if adv.id == id:
                break
        # adv = Advertisements.objects.all()
        context = {'adv': adv, 'id_adv': id}
        return render(request, 'app_advertisements/advertisement.html', context)


def register(request):
    # return HttpResponse('Успешно')
    return render(request, 'app_auth/register.html')


def login(request):
    # return HttpResponse('Успешно')
    return render(request, 'app_auth/login.html')


def profile(request):
    # return HttpResponse('Успешно')
    return render(request, 'app_auth/profile.html')


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

if __name__ == '__main__':
    pass
