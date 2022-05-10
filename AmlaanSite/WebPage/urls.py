from django.contrib import admin
from django.urls import include, path
from WebPage import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
