# Generated by Django 4.0 on 2021-12-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
