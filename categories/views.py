# В наших представлениях (views.py) мы используем функции для обработки запросов и взаимодействия с нашей моделью данных.
# Функция index возвращает рендеринг шаблона index.html без дополнительных параметров.
# Функция cities извлекает все города из модели City и передает их в шаблон cities.html.
# Функция category принимает идентификатор города в качестве параметра, затем извлекает соответствующий город и связанные с ним категории из модели Category.
# Функция service получает идентификатор города и категории, затем извлекает соответствующие услуги из модели Service для заданного города и категории.

from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Category, Service
from django.db.models import Count

def index(request):
    return render(request, 'index.html')

def cities(request):
    cities = City.objects.all()
    return render(request, 'cities.html', {'cities': cities})

def category(request, city_id):
    city = City.objects.get(pk=city_id)
    categories = Category.objects.filter(city=city).annotate(num_masters=Count('service__master')).filter(num_masters__gt=0)
    return render(request, 'category.html', {'city': city, 'categories': categories})

def service(request, city_id, category_id):
    city = City.objects.get(pk=city_id)
    category = Category.objects.get(pk=category_id)
    filtered_services = Service.objects.filter(city=city, category=category).annotate(num_masters=Count('master')).filter(num_masters__gt=0)
    return render(request, 'service.html', {'city': city, 'category': category, 'services': filtered_services})