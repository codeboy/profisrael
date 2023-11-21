# Generated by Django 4.2.7 on 2023-11-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0018_remove_master_gallery_delete_galleryimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/masters')),
            ],
        ),
        migrations.RemoveField(
            model_name='master',
            name='gallery',
        ),
        migrations.AddField(
            model_name='master',
            name='gallery',
            field=models.ManyToManyField(related_name='masters', to='masters.galleryimage', verbose_name='Фото ваших работ'),
        ),
    ]
