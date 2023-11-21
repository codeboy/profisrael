from django.contrib import admin
from .models import City, Category, Service

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    actions = ['clone_city']

    def clone_city(self, request, queryset):
        for city in queryset:
            new_city = City.objects.create(name=city.name + ' (clone)')
            for category in city.category_set.all():
                new_category = Category.objects.create(city=new_city, name=category.name)
                for service in category.service_set.all():
                    Service.objects.create(city=new_city, category=new_category, name=service.name, description=service.description)
        self.message_user(request, "Город успешно клонирован со всеми категориями и услугами")

    clone_city.short_description = "Клонировать выбранные города со всеми категориями и услугами"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [ServiceInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'city')
    list_filter = ('category__city', 'category')
    search_fields = ('name', 'category__name', 'category__city__name')

admin.site.site_header = 'Админка Profisrael'
admin.site.index_title = 'Админка Profisrael'
admin.site.site_title = 'Управление'