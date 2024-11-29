# Generated by Django 5.1.2 on 2024-11-15 13:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspirant', '0004_aspirantprofile_aspirant'),
        ('recruiter', '0005_remove_job_applied_users_job_recruiter'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('aspirant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aspirant.aspirantregistration')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.job')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=255)),
                ('salary_range', models.CharField(max_length=100)),
                ('last_date_to_apply', models.DateField()),
                ('applied_users', models.ManyToManyField(blank=True, related_name='applied_jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]