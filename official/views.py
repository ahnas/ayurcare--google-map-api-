from django.db import models
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from official.forms import BranchForm,DoctorForm,ScheduleForm
from .models import Branch 
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib import messages 
from django.contrib import auth


def log_in(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username is not None and password is not None:
        user=authenticate(username=username, password=password)     
        if user is not None:
            login(request, user)
            return redirect("/official/addBranch/")
        else:   
            messages.error(request, "Invalid Details") 
    else:
        messages.error(request,None) 
    return render (request, 'official/login.html')  


def logout(request):
    auth.logout(request)
    return redirect('official:log_in')

@login_required(login_url='official:log_in')
def addBranch(request):
    branchform = BranchForm(request.POST or None)
    if request.method == 'POST':
        if branchform.is_valid():
           branchform.save()          
           response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Branch Added"
            }
        else:
            print (branchform.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_addBranch" : True,
            "branchform":branchform,
        }
    return render(request, 'official/addBranch.html',context)


@login_required(login_url='official:log_in')
def addDoctor(request):
    doctorform = DoctorForm(request.POST,request.FILES)
    if request.method == 'POST':
        if doctorform.is_valid():
           doctorform.save()          
        response_data = {
            "status" : "true",
            "title" : "Successfully Submitted",
            "message" : "Doctor Added"
        }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_addDoctor" : True,
            "doctorform":doctorform,
        }
    return render(request, 'official/addDoctor.html',context)



@login_required(login_url='official:log_in')
def addSchedule(request):
    scheduleform = ScheduleForm(request.POST or None)
    if request.method == 'POST':
        if scheduleform.is_valid():
           scheduleform.save()          
           response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Schedule Added"
            }
        else:
            
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_addSchedule" : True,
            "scheduleform":scheduleform,
        }
    
    return render(request, 'official/addSchedule.html',context)