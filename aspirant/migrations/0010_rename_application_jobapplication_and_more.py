# Generated by Django 5.1.2 on 2024-11-15 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aspirant', '0009_alter_application_unique_together'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Application',
            new_name='JobApplication',
        ),
        migrations.RemoveField(
            model_name='job',
            name='applied_users',
        ),
    ]
