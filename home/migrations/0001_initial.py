# Generated by Django 2.2.13 on 2024-04-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('Aadhar_number', models.BigIntegerField()),
                ('pan_number', models.CharField(max_length=10)),
            ],
        ),
    ]