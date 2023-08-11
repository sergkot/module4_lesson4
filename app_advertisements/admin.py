from django.contrib import admin
from .models import Advertisements
from advertisement.settings import MEDIA_ROOT


class AdvertisementsAdmin(admin.ModelAdmin):
    readonly_fields = ['image_display', 'img_preview']
    list_display = ['id', 'title', 'description', 'price', 'user', 'img_preview', 'image_display', 'created_date', 'update_date', 'auction']
    # list_display = ['id', 'title', 'description', 'price', 'created_at', 'update_at', 'auction']
    list_filter = ['auction', 'created_at']



admin.site.register(Advertisements, AdvertisementsAdmin)

# Register your models here.
