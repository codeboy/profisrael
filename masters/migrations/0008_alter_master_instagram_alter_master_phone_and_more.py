# Generated by Django 4.2.7 on 2023-11-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0007_master_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='master',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='master',
            name='pricemin',
            field=models.DecimalField(decimal_places=0, max_digits=5, null=True, verbose_name='Цена от'),
        ),
    ]
