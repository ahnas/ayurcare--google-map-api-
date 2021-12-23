from django.db import models
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from .models import Gallery,Treatement,Branch,Doctor,Schedule

def index(request):
    context = {
        "is_index" : True
    }
    return render(request, 'web/index.html',context)

  
def about(request):
    context = {
        "is_about" : True
    }
    return render(request, 'web/aboutus.html',context)


def contact(request):
    context = {
        "is_contact" : True
    }
    return render(request, 'web/contact.html',context)


def galleries(request):
    galleries = Gallery.objects.all()
    context = {
        "is_gallery" : True,
        "galleries" : galleries,
    }
    return render(request,'web/gallery.html',context)


def products(request):
    context = {
        "is_products" : True
    }
    return render(request, 'web/products.html',context)



def doctors(request):
    schedules = Schedule.objects.filter()  
    context = {
        "is_doctors" : True,
        "schedules" : schedules,
    }
    return render(request, 'web/doctor.html',context)


def branch(request):
    context = {
        "is_branch" : True
    }
    return render(request, 'web/branch.html',context)


