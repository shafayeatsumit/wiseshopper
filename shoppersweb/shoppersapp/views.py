from django.shortcuts import render
from .models import ScraperItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def landing_page(request):
    #products=ScraperItem.objects.all()
    return render(request,'shoppersapp/landing_page.html',{})

def mobiles_page(request):
    mobiles_list=ScraperItem.objects.filter(Q(category="mobiles") | Q(category="Mobile Phones"))
    paginator = Paginator(mobiles_list, 25)
    page = request.GET.get('page')
    try:
        mobiles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mobiles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        mobiles = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/mobiles_page.html',{'mobiles': mobiles})

def cars_page(request):
    cars_list=ScraperItem.objects.filter(Q(category='cars')|Q(category="Cars"))
    paginator = Paginator(cars_list, 25)
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cars = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cars = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/cars_page.html',{'cars': cars})

def motorcycles_page(request):
    motorcycles_list=ScraperItem.objects.filter(Q(category='motorcycles')|Q(category='Motorbikes & Scooters'))
    paginator = Paginator(motorcycles_list, 25)
    page = request.GET.get('page')
    try:
        motorcycles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        motorcycles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        motorcycles = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/motorcycles_page.html',{'motorcycles': motorcycles})

def bicycles_page(request):
    bicycles_list=ScraperItem.objects.filter(Q(category='bicycles')|Q(category='Bicycles and Three Wheelers'))
    paginator = Paginator(bicycles_list, 25)
    page = request.GET.get('page')
    try:
        bicycles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bicycles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bicycles = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/bicycles_page.html',{'bicycles': bicycles})

def laptops_page(request):

    laptops_list=ScraperItem.objects.filter(Q(category='laptops')|Q(category='Computers & Tablets'))
    paginator = Paginator(laptops_list, 25)
    page = request.GET.get('page')
    try:
        laptops = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        laptops = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        laptops = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/laptops_page.html',{'laptops':laptops})

def apartments_page(request):

    apartments_list=ScraperItem.objects.filter(Q(category='apartments')|Q(category='Apartments & Flats'))
    paginator = Paginator(apartments_list, 25)
    page = request.GET.get('page')
    try:
        apartments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        apartments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        apartments = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/apartments_page.html',{'apartments':apartments})
