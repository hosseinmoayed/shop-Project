# Generated by Django 4.1 on 2022-08-31 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0007_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='uploads/images/profile/profile.png', null=True, upload_to='images/profile', verbose_name='تصویر آواتار'),
        ),
    ]