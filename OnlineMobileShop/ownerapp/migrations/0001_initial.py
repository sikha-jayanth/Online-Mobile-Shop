# Generated by Django 3.1.2 on 2020-11-10 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=100, unique=True)),
                ('ram', models.CharField(max_length=100)),
                ('internal_storage', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('screen_size', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=1500)),
                ('image', models.ImageField(upload_to='images')),
                ('Mobile_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ownerapp.brand')),
            ],
        ),
    ]
