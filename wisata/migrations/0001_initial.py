# Generated by Django 5.1.3 on 2024-11-30 13:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wisata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('lokasi', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(max_length=1000)),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='wisata')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('review', models.TextField(max_length=1000)),
                ('rating', models.IntegerField(help_text='Rating dari 1 sampai 5', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('wisata', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wisata.wisata')),
            ],
        ),
    ]
