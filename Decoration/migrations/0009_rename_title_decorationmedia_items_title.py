# Generated by Django 5.0.3 on 2024-08-29 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Decoration', '0008_decorationmedia_title_alter_decorationmedia_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='decorationmedia',
            old_name='title',
            new_name='items_title',
        ),
    ]
