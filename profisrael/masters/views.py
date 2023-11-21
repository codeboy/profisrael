from django.shortcuts import render, redirect, get_object_or_404
from .forms import MasterRegistrationForm
from django.http import JsonResponse
from .models import City, Category, Service
from masters.models import Master
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def register_master(request):
    if request.method == 'POST':
        form = MasterRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Обработка валидной формы (сохранение в базу данных и т.д.)
            master = form.save()  # сохраняем мастера и получаем объект
            # Заменяем 'profile_url' на URL для профиля мастера
            return redirect('profile_url', master_id=master.id) 
    else:
        form = MasterRegistrationForm()

    # Ваша логика для получения списка городов, категорий и услуг
    cities = City.objects.all()
    categories = Category.objects.all()
    services = Service.objects.all()

    return render(request, 'registration/registration.html', {'form': form, 'cities': cities, 'categories': categories, 'services': services})

def get_categories_and_services(request):
    city_id = request.GET.get('city_id')
    category_id = request.GET.get('category_id')

    categories = Category.objects.filter(city_id=city_id)
    services = Service.objects.filter(city_id=city_id, category_id=category_id)  # фильтруем услуги по городу и категории
    
    categories_data = [{'id': category.id, 'name': category.name} for category in categories]
    services_data = [{'id': service.id, 'name': service.name} for service in services]

    data = {
        'categories': categories_data,
        'services': services_data,
    }

    return JsonResponse(data)

def master_profile(request, master_id):
    master = get_object_or_404(Master, pk=master_id)
    return render(request, 'profile.html', {'master': master})

def masters_for_service(request, city_id, category_id, service_id):
    city = City.objects.get(pk=city_id)
    category = Category.objects.get(pk=category_id)
    service = Service.objects.get(pk=service_id)
    masters = Master.objects.filter(city=city, category=category, service=service)
    return render(request, 'masters_for_service.html', {'city': city, 'category': category, 'service': service, 'masters': masters})

def all_masters(request):
    masters_list = Master.objects.all()  # получить все записи мастеров
    return render(request, 'masters/all_masters.html', {'masters': masters_list})

def master_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('some-redirect-url')  # перенаправьте пользователя на другую страницу после входа
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})