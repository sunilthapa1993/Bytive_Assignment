# Generated by Django 5.1.4 on 2025-01-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In-Progress', 'In-Progress'), ('Completed', 'Completed')], default='Pending', max_length=11),
        ),
    ]
