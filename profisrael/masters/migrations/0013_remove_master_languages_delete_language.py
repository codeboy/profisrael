# Generated by Django 4.2.7 on 2023-11-18 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0012_alter_language_name_remove_master_languages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='languages',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
