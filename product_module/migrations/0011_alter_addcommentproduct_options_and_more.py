# Generated by Django 4.1 on 2022-09-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0010_addcommentproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addcommentproduct',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterField(
            model_name='addcommentproduct',
            name='message',
            field=models.TextField(verbose_name='متن نظر'),
        ),
    ]