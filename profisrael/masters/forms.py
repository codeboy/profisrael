from django import forms
from .models import Master
from categories.models import City, Category, Service


class MasterRegistrationForm(forms.ModelForm):

    class Meta:
        model = Master
        fields = ['email', 'password', 'name', 'city', 'category', 'service', 'service_name', 'pricemin', 'pricemax', 'address', 'phone', 'whatsapp', 'instagram', 'languages', 'about', 'photo', 'gallery']

    def __init__(self, *args, **kwargs):
        super(MasterRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.all()
        self.fields['category'].queryset = Category.objects.none()
        self.fields['service'].queryset = Service.objects.none()

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['category'].queryset = Category.objects.filter(city_id=city_id)
            except (ValueError, TypeError):
                pass
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['service'].queryset = Service.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.city.category_set
            self.fields['service'].queryset = self.instance.category.service_set