# Generated by Django 3.0.7 on 2021-05-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
