# Generated by Django 4.2.9 on 2024-03-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]