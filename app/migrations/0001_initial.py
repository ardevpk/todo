# Generated by Django 3.2.9 on 2021-11-16 21:45

import autoslug.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsApi',
            fields=[
                ('News_id', models.AutoField(primary_key=True, serialize=False)),
                ('News_image', models.CharField(default='', max_length=1000)),
                ('News_title', models.CharField(default='', max_length=1000)),
                ('News_author', models.CharField(default='', max_length=100)),
                ('News_desc', tinymce.models.HTMLField(default='', max_length=10000000)),
                ('News_slug', autoslug.fields.AutoSlugField(default='', editable=False, populate_from='News_title', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=24)),
                ('Title', models.CharField(default='', max_length=288)),
                ('Desc', tinymce.models.HTMLField(default='', max_length=512)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]