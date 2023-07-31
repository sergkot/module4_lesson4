from django.db import models


class Advertisements(models.Model):
    title = models.CharField("Заголовок",max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=17, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    test_column = models.CharField("test", max_length=100, default='')


    def __str__(self):
        return(f"id={self.id}, title={self.title}, description={self.description}, price={self.price}")


    class Meta:
        db_table = "advertisements"
