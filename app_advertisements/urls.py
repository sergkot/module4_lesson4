from django.urls import path
from .views import index, test_page, top_sellers, advertisement_post, register, login, profile, advertisement
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', index, name='main-page'),
    path('test_page/', test_page),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
    path('advertisement/', advertisement, name='advertisement'),

    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('register/', login, name='register'),
    path('profile/', profile, name='profile'),
    #path('admin/', admin.site.urls),
]
#<int:id>

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

