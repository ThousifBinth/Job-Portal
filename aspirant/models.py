
from django.db import models
from django.contrib.auth.models import User
from recruiter.models import *


class Aspirantregistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def  __str__(self):
        return self.name
    

class AspirantProfile(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    languages_spoken = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)

    # Job Preferences
    desired_job_title = models.CharField(max_length=255, null=True, blank=True)
    job_category = models.CharField(max_length=100, null=True, blank=True)
    location_preference = models.CharField(max_length=255, null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    highest_education_level = models.CharField(max_length=100, null=True, blank=True)
    field_of_study = models.CharField(max_length=200, null=True, blank=True)
    certifications = models.TextField(null=True, blank=True)

    # File uploads
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='cover_letters/', null=True, blank=True)

    # Employment Preferences
    employment_type = models.CharField(max_length=50, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Freelance', 'Freelance')], null=True, blank=True)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    work_availability = models.CharField(max_length=50, null=True, blank=True)
    preferred_working_hours = models.CharField(max_length=50, null=True, blank=True)
    willing_to_relocate = models.BooleanField(default=False)

    # Agreement
    terms_and_conditions = models.BooleanField(default=False)


    aspirant = models.OneToOneField(Aspirantregistration, on_delete=models.CASCADE, related_name='profile',null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Job Profile"
    
# class Job(models.Model):
#     name = models.CharField(max_length=255)  # Name of the job
#     description = models.TextField()  # Job description
#     place = models.CharField(max_length=255)  # Location of the job
#     salary_range = models.CharField(max_length=100)  # Salary range (e.g., "50000-60000 USD")
#     last_date_to_apply = models.DateField()  # Last date to apply for the job
        
#     applied_users = models.ManyToManyField(User, related_name='appliedjobs', blank=True)  # Aspirants who applied for the job

#     def __str__(self):
#         return self.name

    

class JobApplication(models.Model):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]
    
    aspirant = models.ForeignKey(Aspirantregistration, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    # Ensure that an aspirant can only apply to the same job once
    class Meta:
        unique_together = ('aspirant', 'job')

    def __str__(self):
        return f"{self.aspirant.name} - {self.job.name} - {self.status}"

