from django import forms
from django.core.exceptions import ValidationError


class AdvertisementsForm(forms.Form):
    title = forms.CharField(max_length=128,
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    price = forms.DecimalField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    auction = forms.BooleanField(required=False,
                                 widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # user = forms.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))

    def clean_title(self):
        data = self.cleaned_data['title']
        if "?" in data:
            raise forms.ValidationError("В заголовке не должно быть вопросительного знака")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

    # def clean(self):
    #     data = self.cleaned_data['title']
    #     illegal_symbol ="111"
    #     print(f'Проверяем {data} на знак вопоса')
    #     if illegal_symbol in data:
    #         print(f'error {illegal_symbol} in {data}')
    #         #raise ValidationError("В заголовке не должно быть вопросительного знака")
    #         self.add_error('title', "В заголовке не должно быть вопросительного знака")
    #
    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     # return data
