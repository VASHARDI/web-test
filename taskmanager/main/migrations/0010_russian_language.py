# Generated by Django 3.2.5 on 2021-07-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_photo_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='russian_language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Название темы')),
                ('task0', models.TextField(verbose_name='URL-video')),
                ('task1', models.TextField(verbose_name='URL доп. материалов')),
            ],
        ),
    ]
