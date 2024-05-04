# Generated by Django 2.2.13 on 2024-05-03 10:49

from django.db import migrations
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0002_auto_20240503_0709'),
        ('home', '0004_auto_20240503_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='my_state_field',
            field=river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.State'),
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]