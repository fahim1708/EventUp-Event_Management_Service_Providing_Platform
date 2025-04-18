# Generated by Django 5.1.1 on 2024-09-08 05:49

import Decoration.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Decoration', '0015_package_detail_delete_decorationmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_detail',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=Decoration.models.upload_to),
        ),
        migrations.AlterField(
            model_name='package_detail',
            name='media_type',
            field=models.CharField(blank=True, choices=[('image', 'Image'), ('video', 'Video')], max_length=10, null=True),
        ),
    ]
