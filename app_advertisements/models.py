from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import mark_safe
from django.utils.html import format_html
from advertisement.settings import MEDIA_ROOT

User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField("Заголовок",max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=17, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    test_column = models.CharField("test", max_length=100, default='')
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    def __str__(self):
        return(f"id={self.id}, title={self.title}, description={self.description}, price={self.price}")

    class Meta:
        db_table = "advertisements"

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold">'
                'Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата обновления')
    def update_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold">'
                'Сегодня в {}</span>', updated_time
            )
        return self.update_at.strftime('%d.%m.%Y в %H:%M:%S')

    # Вариант1 вывода картинки в админку
    @admin.display(description='Изображение')
    def image_display(self):
        #http://127.0.0.1:8000/media/advertisements/%D0%91%D0%BE%D1%87%D0%BA%D0%B0.jpg
        # print(self.image.name)
        # return(self.image.name)
        media_str = '/media/'
        if self.image:
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(media_str + self.image.name))
            # return mark_safe(f'<img src = "/media/{self.image.name}" width = "200"/>')
        else:
            return('')

    # Вариант2 вывода картинки в админку
    def img_preview(self):  # new
        media_str = '/media/'
        if self.image:
            return mark_safe(f'<img src = "{media_str + self.image.name}" style="max-width:200px; max-height:200px"/>')
        else:
            return ''
