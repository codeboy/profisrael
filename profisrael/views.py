from django.shortcuts import render
from .models import City, Category, Service

def index(request):
    return render(request, 'index.html')

def home(request):
    cities = City.objects.all()
    return render(request, 'home.html', {'cities': cities})

def category(request, city_id):
    city = City.objects.get(pk=city_id)
    categories = Category.objects.filter(city=city)
    return render(request, 'category.html', {'city': city, 'categories': categories})

def service(request, city_id, category_id):
    city = City.objects.get(pk=city_id)
    category = Category.objects.get(pk=category_id)
    services = Service.objects.filter(city=city, category=category)
    return render(request, 'service.html', {'city': city, 'category': category, 'services': services}) 

