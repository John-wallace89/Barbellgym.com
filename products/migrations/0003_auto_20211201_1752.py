# Generated by Django 3.2.9 on 2021-12-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211201_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.TextField(default=True),
        ),
    ]
