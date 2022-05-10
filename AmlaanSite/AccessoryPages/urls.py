from django.urls import include, path
from AccessoryPages import views


urlpatterns = [
    path('', views.productHome, name='productHome'),
    path('<str:slug>', views.products, name='products'),
]
