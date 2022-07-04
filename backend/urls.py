from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('menu.html', views.menu, name='menu'),
    path('book.html', views.book, name='book'),
    path('about.html', views.about, name='about'),
    path('submit', views.submit, name='submit'),
]
