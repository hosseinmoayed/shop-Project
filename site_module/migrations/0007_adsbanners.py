# Generated by Django 4.1 on 2022-09-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0006_slider_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsBanners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان بنر')),
                ('url', models.URLField(blank=True, null=True, verbose_name='آدرس (url)')),
                ('image', models.ImageField(upload_to='images/banners', verbose_name='تصویر بنر')),
                ('position', models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزییات محصول'), ('about_us', 'صفحه درباره ما')], max_length=200, verbose_name='عنوان بنر')),
                ('is_active', models.BooleanField(verbose_name='عنوان بنر')),
            ],
            options={
                'verbose_name': 'بنرتبلیغ',
                'verbose_name_plural': 'بنرهای تبلیغاتی',
            },
        ),
    ]