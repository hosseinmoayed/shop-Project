# Generated by Django 4.1 on 2022-08-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0004_remove_contactus_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaded',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
