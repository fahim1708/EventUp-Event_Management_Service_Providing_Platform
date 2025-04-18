# Generated by Django 5.1.1 on 2024-09-08 05:38

import Decoration.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Decoration', '0014_rename_decoration_review_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10)),
                ('file', models.FileField(upload_to=Decoration.models.upload_to)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Decoration.item')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pack_Details', to='Decoration.package')),
            ],
        ),
        migrations.DeleteModel(
            name='DecorationMedia',
        ),
    ]
