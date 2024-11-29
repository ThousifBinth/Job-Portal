from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from aspirant.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from recruiter.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Aspirantregistration, AspirantProfile





def home(request):
    aspirant = request.session.get('aspirant')  # Get aspirant from the session
    recent_jobs = Job.objects.all().order_by('-created_at')[:4]  # Get the 4 most recent jobs

    # Check if aspirant is logged in or not
    return render(request, 'aspirant/home.html', {
        'aspirant': aspirant,
        'recent_jobs': recent_jobs
    })




def signup(request):
    if request.method == 'POST':
        name1=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Aspirantregistration(name=name1,email=email,password=password)
        customer.save()
        return redirect('aspirant:success')
    return render(request, 'aspirant/signup.html')


def job_profile(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        languages_spoken = request.POST.get('languages_spoken')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        desired_job_title = request.POST.get('desired_job_title')
        job_category = request.POST.get('job_category')
        location_preference = request.POST.get('location_preference')
        years_of_experience = request.POST.get('years_of_experience')
        highest_education_level = request.POST.get('highest_education_level')
        field_of_study = request.POST.get('field_of_study')
        certifications = request.POST.get('certifications')
        employment_type = request.POST.get('employment_type')
        salary_expectation = request.POST.get('salary_expectation')
        work_availability = request.POST.get('work_availability')
        preferred_working_hours = request.POST.get('preferred_working_hours')
        willing_to_relocate = request.POST.get('willing_to_relocate') == 'on'
        terms_and_conditions = request.POST.get('terms_and_conditions') == 'on'
        
        # Handle file uploads
        resume = request.FILES.get('resume')
        cover_letter = request.FILES.get('cover_letter')

        # Validation
        if not first_name or not email or not desired_job_title:
            messages.error(request, "First Name, Email, and Desired Job Title are required.")
            return render(request, 'aspirants/register_job_profile.html')

        # Check if email already exists
        if AspirantProfile.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'aspirants/register_job_profile.html')

        # Create and save the job profile
        profile = AspirantProfile(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            nationality=nationality,
            languages_spoken=languages_spoken,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            postal_code=postal_code,
            desired_job_title=desired_job_title,
            job_category=job_category,
            location_preference=location_preference,
            years_of_experience=years_of_experience,
            highest_education_level=highest_education_level,
            field_of_study=field_of_study,
            certifications=certifications,
            employment_type=employment_type,
            salary_expectation=salary_expectation,
            work_availability=work_availability,
            preferred_working_hours=preferred_working_hours,
            willing_to_relocate=willing_to_relocate,
            terms_and_conditions=terms_and_conditions,
            resume=resume,
            cover_letter=cover_letter
        )
        profile.save()

        messages.success(request, "Your job profile has been created successfully!")
        return redirect('dashboard')

    return render(request, 'aspirants/job_profile.html')







def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            # Check if aspirant with this email and password exists
            aspirant = Aspirantregistration.objects.get(email=email, password=password)

            # Set the session for aspirant_id
            request.session['aspirant_id'] = aspirant.id

            # Check if the aspirant has a profile
            if hasattr(aspirant, 'profile') and aspirant.profile:
                # If profile exists, redirect to dashboard
                return redirect('aspirant:dashboard')
            else:
                # If profile does not exist, redirect to register page
                messages.info(request, "Please complete your profile.")
                return redirect('aspirant:register')

        except Aspirantregistration.DoesNotExist:
            # No aspirant found with the given email and password
            messages.error(request, "Invalid email or password.")
            return redirect('aspirant:login')

    return render(request, 'aspirant/login.html')











def register(request):
    if request.method == 'POST':
        # First, ensure that the user is logged in (use session or authentication)
        if 'aspirant_id' not in request.session:
            messages.error(request, "You need to be logged in to create a profile.")
            return redirect('aspirant:login')

        # Get the logged-in aspirant user object
        aspirant = Aspirantregistration.objects.get(id=request.session['aspirant_id'])

        # Collect the POST data from the form submission
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        languages_spoken = request.POST.get('languages_spoken')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')

        desired_job_title = request.POST.get('desired_job_title')
        job_category = request.POST.get('job_category')
        location_preference = request.POST.get('location_preference')
        years_of_experience = request.POST.get('years_of_experience')
        highest_education_level = request.POST.get('highest_education_level')
        field_of_study = request.POST.get('field_of_study')
        certifications = request.POST.get('certifications')

        employment_type = request.POST.get('employment_type')
        salary_expectation = request.POST.get('salary_expectation')
        work_availability = request.POST.get('work_availability')
        preferred_working_hours = request.POST.get('preferred_working_hours')
        willing_to_relocate = request.POST.get('willing_to_relocate') == 'on'  # Checkbox returns 'on'
        terms_and_conditions = request.POST.get('terms_and_conditions') == 'on'  # Checkbox returns 'on'

        # Handle file uploads (resume and cover letter)
        resume = request.FILES.get('resume')
        cover_letter = request.FILES.get('cover_letter')

        # Validate form data manually (you can add more validation as needed)
        if not first_name or not email:
            messages.error(request, "First name and email are required.")
            return render(request, 'aspirant/profile_form.html')

        # Create the profile object
        profile = AspirantProfile(
            aspirant=aspirant,  # Link the profile to the logged-in aspirant
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            nationality=nationality,
            languages_spoken=languages_spoken,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            postal_code=postal_code,
            desired_job_title=desired_job_title,
            job_category=job_category,
            location_preference=location_preference,
            years_of_experience=years_of_experience,
            highest_education_level=highest_education_level,
            field_of_study=field_of_study,
            certifications=certifications,
            employment_type=employment_type,
            salary_expectation=salary_expectation,
            work_availability=work_availability,
            preferred_working_hours=preferred_working_hours,
            willing_to_relocate=willing_to_relocate,
            terms_and_conditions=terms_and_conditions,
            resume=resume,
            cover_letter=cover_letter,
        )

        # Save the profile
        try:
            profile.save()
            messages.success(request, "Profile created successfully!")
            return redirect('aspirant:dashboard')  # Redirect to a success page or dashboard
        except ValidationError as e:
            messages.error(request, f"Error saving profile: {e}")
            return render(request, 'aspirant/register.html')

    else:
        # If GET request, display the form
        return render(request, 'aspirant/register.html')

def success(request):
    return render(request, 'aspirant/success.html')






def dashboard(request):
     if 'aspirant_id' in request.session:
        aspirant_name = request.session.get('aspirant_name')
        jobs = Job.objects.all()
        return render(request,'aspirant/dashboard.html', {'jobs':jobs,'username': aspirant_name})
     else:
        return redirect('aspirant:login')





def jobdetail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # Check if the aspirant is logged in
    aspirant_id = request.session.get('aspirant_id')
    if aspirant_id:
        aspirant = get_object_or_404(Aspirantregistration, id=aspirant_id)

        # Check if the aspirant has already applied for this job
        has_applied = JobApplication.objects.filter(aspirant=aspirant, job=job).exists()
    else:
        has_applied = False  # No aspirant logged in, can't apply

    return render(request, 'aspirant/jobdetail.html', {'job': job, 'has_applied': has_applied})








def apply_for_job(request, job_id):
    # Check if the aspirant is logged in via session
    if 'aspirant_id' not in request.session:
        messages.error(request, "You must be logged in to apply for a job.")
        return redirect('aspirant:login')  # Redirect to login page if not logged in

    aspirant_id = request.session['aspirant_id']
    
    # Corrected line: Use `id` instead of `aspirant_id`
    aspirant = get_object_or_404(Aspirantregistration, id=aspirant_id)

    # Get the job object
    job = get_object_or_404(Job, id=job_id)

    # Check if the aspirant has already applied for this job
    if JobApplication.objects.filter(aspirant=aspirant, job=job).exists():
        messages.error(request, "You have already applied for this job.")
        return redirect('aspirant:jobdetail', job_id=job.id)  # Redirect back to job detail page

    # Create a new job application (default status is 'Pending')
    JobApplication.objects.create(aspirant=aspirant, job=job)

    # Show a success message and redirect back to the job detail page
    messages.success(request, 'Job application submitted successfully!')
    return redirect('aspirant:jobdetail', job_id=job.id)  # Redirect back to job detail page




def profile(request):
    aspirant_id = request.session.get('aspirant_id')
    if not aspirant_id:
        return redirect('aspirant:login')
    
    # Get the aspirant and their profile
    try:
        aspirant = Aspirantregistration.objects.get(id=aspirant_id)
        profile = aspirant.profile  # Access related profile
        return render(request, 'aspirant/profile.html', {'profile': profile})
    except Aspirantregistration.DoesNotExist:
        return redirect('aspirant:login')





def editprofile(request):
    # Get the aspirant ID from the session
    aspirant_id = request.session.get('aspirant_id')
    if not aspirant_id:
        return redirect('aspirant:login')  # If not logged in, redirect to login page

    aspirant = get_object_or_404(Aspirantregistration, id=aspirant_id)
    profile = aspirant.profile  # Access related profile object

    if request.method == 'POST':
        # Get data from the form
        profile.first_name = request.POST.get('first_name', profile.first_name)
        profile.last_name = request.POST.get('last_name', profile.last_name)
        profile.email = request.POST.get('email', profile.email)
        profile.phone_number = request.POST.get('phone_number', profile.phone_number)
        profile.address = request.POST.get('address', profile.address)
        profile.city = request.POST.get('city', profile.city)
        profile.postal_code = request.POST.get('postal_code', profile.postal_code)
        profile.desired_job_title = request.POST.get('desired_job_title', profile.desired_job_title)
        profile.job_category = request.POST.get('job_category', profile.job_category)
        profile.location_preference = request.POST.get('location_preference', profile.location_preference)
        profile.years_of_experience = request.POST.get('years_of_experience', profile.years_of_experience)
        profile.highest_education_level = request.POST.get('highest_education_level', profile.highest_education_level)
        profile.field_of_study = request.POST.get('field_of_study', profile.field_of_study)
        profile.certifications = request.POST.get('certifications', profile.certifications)
        profile.employment_type = request.POST.get('employment_type', profile.employment_type)
        profile.salary_expectation = request.POST.get('salary_expectation', profile.salary_expectation)
        profile.work_availability = request.POST.get('work_availability', profile.work_availability)
        profile.preferred_working_hours = request.POST.get('preferred_working_hours', profile.preferred_working_hours)
        profile.willing_to_relocate = 'willing_to_relocate' in request.POST
        profile.terms_and_conditions = 'terms_and_conditions' in request.POST

        # Handle file uploads
        if 'resume' in request.FILES:
            profile.resume = request.FILES['resume']
        if 'cover_letter' in request.FILES:
            profile.cover_letter = request.FILES['cover_letter']

        profile.save()  # Save the updated profile

        messages.success(request, "Your profile has been updated successfully!")
        return redirect('aspirant:profile')  # Redirect to the profile page after successful update

    return render(request, 'aspirant/editprofile.html', {'profile': profile})






def appliedjobs(request):
    # Check if the aspirant is logged in via session
    aspirant_id = request.session.get('aspirant_id')
    
    if not aspirant_id:
        # If not logged in, redirect to login page
        messages.error(request, "You must be logged in to view your applied jobs.")
        return redirect('aspirant:login')  # Adjust the login URL name as needed
    
    # Get the aspirant instance
    aspirant = get_object_or_404(Aspirantregistration, id=aspirant_id)

    # Get all jobs that the aspirant has applied for
    applied_jobs = JobApplication.objects.filter(aspirant=aspirant)

    # Pass the jobs to the template
    return render(request, 'aspirant/appliedjobs.html', {'applied_jobs': applied_jobs})




def search(request):
    # Check if the aspirant is logged in via session
    if 'aspirant_id' not in request.session:
        messages.error(request, "You must be logged in to search for jobs.")
        return redirect('aspirant:login')  # Redirect to login page if not logged in

    jobs = []  # Initialize an empty list to store search results
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # Perform a search on the 'name' field of Job model
            jobs = Job.objects.filter(name__icontains=keyword)

    return render(request, 'aspirant/dashboard.html', {'jobs': jobs})







# def search(request):
#     jobs = []  # Initialize an empty list to store search results
#     if 'keyword' in request.GET:
#         keyword = request.GET['keyword']
#         if keyword:
#             # Perform a search on the 'name' field only
#             jobs = Job.objects.filter(name__icontains=keyword)

#     return render(request, 'aspirant/dashboard.html', {'jobs': jobs})




def logout(request):
    # Remove both aspirant_id and aspirant_name from the session
    if 'aspirant_id' in request.session:
        del request.session['aspirant_id']
    if 'aspirant_name' in request.session:
        del request.session['aspirant_name']
    
    # Redirect to the login page or home page
    return redirect('aspirant:login')  # Ensure this points to your login page
