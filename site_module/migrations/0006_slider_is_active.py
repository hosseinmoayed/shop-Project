# Generated by Django 4.1 on 2022-08-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0005_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]