# Generated by Django 4.2.7 on 2023-11-20 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0022_remove_master_gallery_delete_photo_master_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='gallery',
            field=models.ImageField(upload_to='media/gallery', verbose_name='Фото ваших работ'),
        ),
        migrations.CreateModel(
            name='GalleryPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profisrael/static/images/')),
                ('master', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='masters.master', verbose_name='Master')),
            ],
        ),
    ]
