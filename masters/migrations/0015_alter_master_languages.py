# Generated by Django 4.2.7 on 2023-11-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0014_master_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='languages',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Языки помимо русского'),
        ),
    ]
