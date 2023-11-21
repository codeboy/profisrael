from django import forms
from django.contrib import admin
from .models import Master
from import_export.admin import ImportExportActionModelAdmin

class MasterAdminForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = '__all__'
        widgets = {
            'about': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        }

class MasterAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'category', 'service', 'languages')  
    form = MasterAdminForm

admin.site.register(Master, MasterAdmin)