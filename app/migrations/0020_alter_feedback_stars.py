# Generated by Django 4.1.5 on 2023-03-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='stars',
            field=models.FloatField(),
        ),
    ]
