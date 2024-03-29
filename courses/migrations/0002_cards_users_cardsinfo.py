# Generated by Django 4.1 on 2022-08-18 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('level', models.IntegerField(verbose_name='level')),
                ('content', models.TextField(verbose_name='content')),
            ],
            options={
                'db_table': 'cards',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('level', models.IntegerField(verbose_name='level')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='CardsInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('card_info', models.TextField(verbose_name='info')),
                ('card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.cards', verbose_name='card')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.users', verbose_name='user')),
            ],
            options={
                'db_table': 'cards_info',
            },
        ),
    ]
