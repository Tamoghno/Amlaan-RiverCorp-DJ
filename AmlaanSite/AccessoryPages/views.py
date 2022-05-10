from django.shortcuts import render, HttpResponse

# Create your views here.


def productHome(request):
    return HttpResponse('It is us, the product Homepage')


def products(request, slug):
    return HttpResponse(f'It is us, products page {slug}')
