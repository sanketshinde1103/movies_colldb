# Generated by Django 3.2 on 2021-05-03 10:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('genres', models.ManyToManyField(to='movies_collection.Genre')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('movies', models.ManyToManyField(to='movies_collection.Movie')),
            ],
            options={
                'db_table': 'collection',
            },
        ),
    ]
