# Generated by Django 4.1 on 2022-08-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_footercategorylink_alter_sitesetting_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='footercategorylink',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]