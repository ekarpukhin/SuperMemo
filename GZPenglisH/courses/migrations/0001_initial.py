# Generated by Django 4.0.4 on 2022-04-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('anons', models.CharField(max_length=250, verbose_name='О курсе')),
                ('text_all', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
