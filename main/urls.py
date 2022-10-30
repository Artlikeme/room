from django.urls import path
from . import views

urlpatterns = [
    path('', views.maintest,name='main'),
    path('forms/', views.delete,name='delete'),
    path('find/', views.find,name='find'),
]