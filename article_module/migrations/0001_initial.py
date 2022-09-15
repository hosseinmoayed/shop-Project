# Generated by Django 4.1 on 2022-08-29 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان مقاله')),
                ('url_title', models.CharField(max_length=200, verbose_name='عنوان (url)')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecategory', verbose_name='زیر مجموعه')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
    ]
