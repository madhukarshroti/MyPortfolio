# Generated by Django 3.2 on 2023-02-04 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Project',
        ),
    ]
