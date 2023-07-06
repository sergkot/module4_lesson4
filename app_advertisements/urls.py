from django.urls import path
from .views import index, test_page

urlpatterns = [
    path('user/', index),
    path('test_page/', test_page)
]