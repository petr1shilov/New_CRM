from django import forms
from django.shortcuts import render
from .models import User_request
from .forms import UserForm



def index(request):
    tasks = User_request.objects.all()
    tasks = User_request.objects.order_by('-pub_time')
    return render(request, "user_reqest\index.html", {'title': 'Список запросов', 'tasks': tasks}) # так же можно делать сортировку и срез

def for_data(request): 
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Error'


    form = UserForm()
    context = {
        'form' : form,
        'error': error
    }
    return render(request, "user_reqest\if_db.html", context)

