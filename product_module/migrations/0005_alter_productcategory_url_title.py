# Generated by Django 4.1 on 2022-09-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_productcategory_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='url_title',
            field=models.CharField(db_index=True, max_length=300, unique=True, verbose_name='عنوان (url)'),
        ),
    ]