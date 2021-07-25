from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='list'),
    path('requests', views.for_data, name='add list')
]
