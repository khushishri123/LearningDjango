# Generated by Django 4.1.7 on 2023-07-12 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='product',
            name='promotion',
        ),
    ]