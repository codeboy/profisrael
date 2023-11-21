from django.db import models
from django.views import View
from django.http import JsonResponse
from categories.models import City, Category, Service


class GalleryPicture(models.Model):
    image = models.ImageField(upload_to='profisrael/static/images/')
    master = models.ForeignKey("Master", verbose_name="Master", on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
         return self.image.url


class Master(models.Model):
    email = models.EmailField(unique=True, verbose_name='Почта', null=True, blank=False)
    password = models.CharField(max_length=100, verbose_name='Пароль', blank=False)
    name = models.CharField(max_length=100, verbose_name='Имя', blank=False)
    city = models.ForeignKey('categories.City', on_delete=models.CASCADE, verbose_name='Город')
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, verbose_name='Категория')
    service = models.ForeignKey('categories.Service', on_delete=models.CASCADE, verbose_name='Услуга')
    service_name = models.CharField(max_length=255, verbose_name='Название услуги', null=False, blank=False) 
    pricemin = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Цена от', null=True, blank=False)
    pricemax = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Цена до', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True) 
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True, blank=False) 
    whatsapp = models.CharField(max_length=20, verbose_name='WhatsApp', null=True, blank=True) 
    instagram = models.CharField(max_length=100, verbose_name='Instagram', null=True, blank=True)
    languages = models.CharField(max_length=100, verbose_name='Языки помимо русского', null=True, blank=True)
    about = models.TextField(blank=False)
    photo = models.ImageField(upload_to='media/masters', verbose_name='Фото', blank=False) 
    gallery = models.ImageField(upload_to='media/gallery', verbose_name='Фото ваших работ', null=True, blank=True) # Поле изменить на multi pics
    
    def __str__(self):
        return self.name

    
class GetServicesView(View):
    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category')
        city_id = request.GET.get('city')
        # Получаем данные о новом списке услуг
        services = Service.objects.filter(category__id=category_id, city__id=city_id)
        services_data = [{'id': service.id, 'name': service.name} for service in services]
        return JsonResponse(services_data, safe=False)
    