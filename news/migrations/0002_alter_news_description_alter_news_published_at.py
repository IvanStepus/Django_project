# Generated by Django 4.2.1 on 2023-06-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
