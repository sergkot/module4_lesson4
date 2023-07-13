from django.urls import path
from .views import index, test_page, top_sellers, advertisement_post, register

urlpatterns = [
    path('', index, name='main-page'),
    path('test_page/', test_page),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
    path('register/', register, name='register'),
]
