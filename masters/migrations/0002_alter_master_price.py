# Generated by Django 4.2.7 on 2023-11-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]