

from django.urls import path
from . import views

app_name = 'recruiter'

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addjobs/',views.addjobs,name='addjobs'),
    path('manageapplications/', views.manageapplications, name='manageapplications'),
    path('accept-application/<int:application_id>/', views.accept_application, name='accept_application'),
    path('reject-application/<int:application_id>/', views.reject_application, name='reject_application'),
    path('editjob/<int:job_id>/', views.editjobs, name='editjobs')
    # path('view-profile/<int:application_id>/', views.view_profile, name='view_profile'),
]



