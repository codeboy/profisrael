# Generated by Django 4.2.7 on 2023-11-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0006_remove_master_price_master_phone_master_pricemax_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='instagram',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Instagram'),
        ),
    ]
