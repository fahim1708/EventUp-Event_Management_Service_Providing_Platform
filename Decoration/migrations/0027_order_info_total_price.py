# Generated by Django 5.0.3 on 2024-10-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Decoration', '0026_order_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_info',
            name='total_Price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
