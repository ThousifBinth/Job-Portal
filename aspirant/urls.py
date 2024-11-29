from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
# importing views from current directory


app_name='aspirant'


urlpatterns= [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('success/',views.success,name='success'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('job/<int:job_id>/', views.jobdetail, name='jobdetail'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    # path('profile/', views.profile, name='profile'),  
    path('appliedjobs/', views.appliedjobs, name='appliedjobs'), 
    # path('profile/<int:aspirant_id>/', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('logout/', views.logout, name='logout'),
    path('editprofile/', views.editprofile, name='editprofile')

]  

