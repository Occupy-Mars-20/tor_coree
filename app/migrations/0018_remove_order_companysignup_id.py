# Generated by Django 4.1.5 on 2023-03-02 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_order_companysignup_id_alter_order_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='companysignup_id',
        ),
    ]
