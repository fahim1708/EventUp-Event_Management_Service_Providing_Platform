# Generated by Django 5.0.3 on 2024-09-11 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Decoration', '0020_rename_item_id_item_id_rename_package_id_package_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='ID',
            new_name='Item_ID',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='ID',
            new_name='package_id',
        ),
    ]
