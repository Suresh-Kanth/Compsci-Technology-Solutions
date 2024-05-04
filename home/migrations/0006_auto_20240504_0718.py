# Generated by Django 2.2.13 on 2024-05-04 07:18

from django.db import migrations, models
import django.db.models.deletion
import river.models.fields.state
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20240503_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='no',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, unique=True, verbose_name='Employee Number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='my_state_field',
            field=river.models.fields.state.StateField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.State'),
        ),
    ]