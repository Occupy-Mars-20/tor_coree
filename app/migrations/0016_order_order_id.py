# Generated by Django 4.1.5 on 2023-02-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default=2, max_length=9),
            preserve_default=False,
        ),
    ]