from .models import User_request
from django.forms import ModelForm, TextInput, Textarea,fields, widgets

class UserForm(ModelForm):
    class Meta:
        model = User_request
        fields = ["user_name", "text_1", "user_conact", "pub_time", "pub_date"]
        widgets = {
        "user_name": TextInput(attrs={
            'class': 'from-control',
            'placeholder': 'Введите ФИО'
            }),
        "text_1": Textarea(attrs={
            'class': 'from-control',
            'placeholder': 'Опишите запрос'
            }),
            "user_conact": TextInput(attrs={
            'class': 'from-control',
            'placeholder': 'Введите контанктные данные'
            }),
            "pub_time": TextInput(attrs={
            'class': 'from-control',
            'placeholder': 'Введите время'
            }),
            "pub_date": TextInput(attrs={
            'class': 'from-control',
            'placeholder': 'Введите дату'
            }),
        }



    # user_name = models.CharField('name', max_length=50)
    # user_conact = models.CharField('contact', max_length=50)
    # text_1 = models.TextField('text')
    # pub_time = models.TimeField('time')
    # pub_date = models.DateField('date')