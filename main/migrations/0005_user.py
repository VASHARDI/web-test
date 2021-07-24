
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000, verbose_name='Название')),
                ('task', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
