# Generated by Django 4.2.7 on 2023-11-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0003_customuser_remove_master_portfolio_photos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email address'),
        ),
    ]
