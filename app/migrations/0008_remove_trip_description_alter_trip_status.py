# Generated by Django 4.1.5 on 2023-02-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='description',
        ),
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
