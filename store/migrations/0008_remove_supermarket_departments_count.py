# Generated by Django 4.2.1 on 2023-06-08 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_supermarket_departments_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supermarket',
            name='departments_count',
        ),
    ]
