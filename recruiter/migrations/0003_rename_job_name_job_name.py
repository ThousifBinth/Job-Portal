# Generated by Django 5.1.2 on 2024-11-14 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0002_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_name',
            new_name='name',
        ),
    ]