# Generated by Django 4.0.5 on 2022-06-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='x', max_length=255, verbose_name='Автор поста')),
                ('avatar', models.CharField(default='x', max_length=1023, verbose_name='Аватарка автора')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.CharField(max_length=255, verbose_name='Текст')),
                ('image_url', models.CharField(max_length=1023, verbose_name='URL-картинки')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MainPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.CharField(max_length=255, verbose_name='Текст')),
                ('image_url', models.CharField(max_length=1023, verbose_name='URL-картинки')),
            ],
        ),
    ]
