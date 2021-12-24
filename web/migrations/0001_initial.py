# Generated by Django 4.0 on 2021-12-23 10:22

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_number', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='doctors')),
                ('qualification', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Galleries')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Treatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Treatment')),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.branch')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.doctor')),
                ('treatement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.treatement')),
            ],
        ),
    ]