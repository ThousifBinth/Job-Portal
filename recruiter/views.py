from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from aspirant.models import*


# Create your views here.





def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if Recruiterregistration.objects.filter(name=name, email=email, password=password).exists():
            return redirect('recruiter:dashboard')
        else:
            return render(request, 'recruiter/login.html', {'msg': 'Invalid email or password'})
    return render(request, 'recruiter/login.html')




def addjobs(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        description = request.POST.get('description')
        place = request.POST.get('place')
        salary_range = request.POST.get('salary_range')
        last_date_to_apply = request.POST.get('last_date_to_apply')
        
        # Validation (you can add more validation if needed)
        if not name or not description or not place or not salary_range or not last_date_to_apply:
            messages.error(request, "All fields are required.")
            return render(request, 'recruiter/dashboard.html')

        # Create and save the job object
        job = Job(
            name=name,
            description=description,
            place=place,
            salary_range=salary_range,
            last_date_to_apply=last_date_to_apply
        )
        job.save()

        messages.success(request, "Job listing created successfully!")
        return redirect('recruiter:dashboard')  # Redirect to a success page after saving

    return render(request, 'recruiter/addjobs.html')





def dashboard(request):
    jobs = Job.objects.all()
    return render(request,'recruiter/dashboard.html',{'jobs': jobs})

# views.py


def manageapplications(request):
    # Fetch all job applications, regardless of status
    applications = JobApplication.objects.all()

    return render(request, 'recruiter/manageapplications.html', {
        'applications': applications,
    })




def accept_application(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)

    if application.status == JobApplication.PENDING:
        application.status = JobApplication.ACCEPTED
        application.save()
        messages.success(request, f"Application for {application.job.name} has been accepted.")
    else:
        messages.error(request, "This application has already been processed.")
    
    return redirect('recruiter:manageapplications')

def reject_application(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)

    if application.status == JobApplication.PENDING:
        application.status = JobApplication.REJECTED
        application.save()
        messages.success(request, f"Application for {application.job.name} has been rejected.")
    else:
        messages.error(request, "This application has already been processed.")
    
    return redirect('recruiter:manageapplications')


# def view_profile(request, application_id):
#     application = get_object_or_404(JobApplication, id=application_id)
#     profile = application.aspirant.profile  # Assuming an aspirant has a profile
#     return render(request, 'recruiter/view_profile.html', {'profile': profile})


def deletejobs(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('recruiter:dashboard')



def editjobs(request, job_id):
    # Get the job object by ID (or return 404 if it doesn't exist)
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        # Get updated data from the form
        name = request.POST.get('name')
        description = request.POST.get('description')
        place = request.POST.get('place')
        salary_range = request.POST.get('salary_range')
        last_date_to_apply = request.POST.get('last_date_to_apply')

        # Validation (you can add more validation if needed)
        if not name or not description or not place or not salary_range or not last_date_to_apply:
            messages.error(request, "All fields are required.")
            return render(request, 'recruiter/editjobs.html', {'job': job})

        # Update the job object with the new values
        job.name = name
        job.description = description
        job.place = place
        job.salary_range = salary_range
        job.last_date_to_apply = last_date_to_apply
        job.save()

        messages.success(request, "Job listing updated successfully!")
        return redirect('recruiter:dashboard')  # Redirect to the dashboard after updating

    # If GET request, display the current job details in the form
    return render(request, 'recruiter/editjobs.html', {'job': job})

