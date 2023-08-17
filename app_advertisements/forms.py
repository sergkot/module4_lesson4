from django import forms


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
