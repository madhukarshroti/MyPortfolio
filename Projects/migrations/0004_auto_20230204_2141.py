# Generated by Django 3.2 on 2023-02-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_rename_prject_name_project_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='Project/images')),
                ('Feature1', models.CharField(max_length=50)),
                ('Feature2', models.CharField(max_length=50)),
                ('Feature3', models.CharField(max_length=50)),
                ('Feature4', models.CharField(max_length=50)),
                ('Feature5', models.CharField(max_length=50)),
                ('project_name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
