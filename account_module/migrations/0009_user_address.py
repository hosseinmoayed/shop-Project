# Generated by Django 4.1 on 2022-09-01 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0008_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
    ]
