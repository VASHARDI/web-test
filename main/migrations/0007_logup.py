# Generated by Django 3.2.5 on 2021-07-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='logup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Версия сайта')),
            ],
        ),
    ]
