# Generated by Django 4.1 on 2022-09-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0008_alter_adsbanners_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsbanners',
            name='position',
            field=models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزییات محصول'), ('about_us', 'صفحه درباره ما')], max_length=200, verbose_name='محل قرار گیری'),
        ),
    ]
