# Generated by Django 4.2.1 on 2023-06-04 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_department_market'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supermarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_create', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('floor', models.IntegerField()),
                ('date_of_create', models.DateField()),
                ('departments', models.ManyToManyField(to='store.department')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Market',
        ),
    ]
