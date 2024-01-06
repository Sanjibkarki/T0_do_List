# Generated by Django 4.2.5 on 2024-01-06 09:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_register_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='adde_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='due_dates',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]