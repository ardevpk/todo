# Generated by Django 3.2.9 on 2021-11-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_newsapi_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='User',
            field=models.CharField(default='', max_length=16),
        ),
    ]
