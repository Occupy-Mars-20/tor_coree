# Generated by Django 4.1.5 on 2023-03-02 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_order_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderid', to='app.order'),
        ),
    ]