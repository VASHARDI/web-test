# Generated by Django 3.2.5 on 2021-07-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000, verbose_name='Название темы')),
                ('task0', models.TextField(verbose_name='URL-video')),
                ('task1', models.TextField(verbose_name='URL доп.материалов')),
            ],
        ),
    ]
