from django.contrib import admin
from django.urls import path
from categories import views as cat_views  # Псевдоним для избежания конфликта имен
from masters.views import all, register_master, get_categories_and_services, masters_for_service, master_profile, editprofile, master_login, online, contact, error, help
from django.conf import settings
from django.conf.urls.static import static
from masters import views
from schema_graph.views import Schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cat_views.index, name='index'),
    path('cities/', cat_views.cities, name='cities'),
    path('cities/<int:city_id>/', cat_views.category, name='category'),
    path('cities/<int:city_id>/<int:category_id>/', cat_views.service, name='service'),
    path('registration/', register_master, name='registration'),  # Без импорта из masters.views, так как он уже импортирован вверху
    path('get_categories_and_services/', get_categories_and_services, name='get_categories_and_services'),
    path('<int:master_id>/', master_profile, name='profile_url'),  # Изменили URL для профиля мастера  # Просто используем импортированное представление
    path('masters/<int:city_id>/<int:category_id>/<int:service_id>/', views.masters_for_service, name='masters_for_service'),
    path('login/', master_login, name='master-login'),  # Используем master_login напрямую
    path('schema/', Schema.as_view()),
    path('all/', all, name='all'),
    path('online/', online, name='online'), 
    path('contact/', contact, name='contact'),
    path('editprofile/', editprofile, name='editprofile'),
    path('error/', error, name='error'),
    path('help/', help, name='help'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)