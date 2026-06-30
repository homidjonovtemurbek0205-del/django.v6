from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-book/', views.add_book, name='add_book'),
    path('success/', views.success, name='success'),
]
