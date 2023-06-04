# Generated by Django 4.2.1 on 2023-06-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_description_alter_news_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='timestamp',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(help_text='200 letters', max_length=200, unique_for_date='published_at', verbose_name='Название'),
        ),
    ]