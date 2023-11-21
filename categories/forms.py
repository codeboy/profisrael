from django import forms
from .models import City, Category, Service

class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ServiceAdminForm, self).__init__(*args, **kwargs)
        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['category'].queryset = Category.objects.filter(city_id=city_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.city.category_set