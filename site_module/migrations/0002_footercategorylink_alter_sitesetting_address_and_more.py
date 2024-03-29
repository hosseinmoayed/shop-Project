# Generated by Django 4.1 on 2022-08-29 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterCategoryLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی لینک',
                'verbose_name_plural': 'دسته بندی لینک ها',
            },
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='address',
            field=models.TextField(verbose_name='آدرس '),
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('url', models.URLField(max_length=600, verbose_name='ادرس لینک')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_module.footercategorylink', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': ' لینک فوتر',
                'verbose_name_plural': ' لینک فوتر',
            },
        ),
    ]
