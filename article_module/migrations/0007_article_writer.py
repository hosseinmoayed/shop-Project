# Generated by Django 4.1 on 2022-08-29 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0006_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.CharField(default='ادمین', max_length=100, verbose_name='نویسنده'),
        ),
    ]