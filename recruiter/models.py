from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recruiterregistration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def  __str__(self):
        return self.name
    

class Job(models.Model):
    name = models.CharField(max_length=255)  # Name of the job
    description = models.TextField()  # Job description
    place = models.CharField(max_length=255)  # Location of the job
    salary_range = models.CharField(max_length=100)  # Salary range
    last_date_to_apply = models.DateField()  # Last date to apply
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)  # Automatically set the creation timestamp

    # recruiter = models.ForeignKey(Recruiterregistration, on_delete=models.CASCADE, related_name='jobs',null=True,blank=True)  # Link to recruiter

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

