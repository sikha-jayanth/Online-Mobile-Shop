# Generated by Django 3.1.2 on 2020-11-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=120)),
                ('user', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
