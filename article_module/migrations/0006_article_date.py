# Generated by Django 4.1 on 2022-08-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0005_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان انتشار'),
        ),
    ]