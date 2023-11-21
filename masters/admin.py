from django import forms
from django.contrib import admin
from .models import Master, GalleryPicture
from import_export.admin import ImportExportActionModelAdmin


class GalleryPictureAdmin(admin.StackedInline):
    model = GalleryPicture


class MasterAdminForm(forms.ModelForm):
    
    class Meta:
        model = Master
        fields = '__all__'
        widgets = {
            'about': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        }


class MasterAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    
    inlines = [GalleryPictureAdmin]
    list_display = ('id', 'name', 'city', 'category', 'service')  
    form = MasterAdminForm
    search_fields = ['id']

admin.site.register(Master, MasterAdmin)


# class PostImageAdmin(admin.ModelAdmin):
    # pass
