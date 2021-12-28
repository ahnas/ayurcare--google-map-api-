from django.urls import path
from official.views import *
 
app_name = 'official' 

urlpatterns = [

    path('',log_in,name="log_in"),
    path('logout/', logout, name='logout'),
    path('addBranch/',addBranch,name="addBranch"),
    path('addDoctor/',addDoctor,name="addDoctor"),
    path('addSchedule/',addSchedule,name="addSchedule"),
    
]