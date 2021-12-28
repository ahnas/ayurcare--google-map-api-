from django.db import models
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from web.models import Gallery,Treatement
from official.models import Doctor,Schedule
from .forms import ContactForm


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
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Message successfully updated"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            'is_contact' : True,
            'form' : form,
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
    schedule = Schedule.objects.all()
    
    context = {
        "is_doctors" : True,
        
        "schedule":schedule,
    }
    return render(request, 'web/doctor.html',context)


def branch(request):
    context = {
        "is_branch" : True
    }
    return render(request, 'web/branch.html',context)


def book(request,slug):
    schedule = get_object_or_404(Schedule,slug=slug)
    if request.POST:
        ptname = request.POST['ptname']
        ptnumber = request.POST['ptnumber']
        start = schedule.start_time.strftime("%I:%M %p")
        end = schedule.end_time.strftime("%I:%M %p")

        whatsappbtn = 'https://wa.me/+91'+str(schedule.branch.phone)

        messagestring = '?text=Patient Name : '+ptname+'%0aPatient Number : '+ptnumber+\
                "%0a*-----Booking Details------*"

        messagestring += '%0aBranch : '+schedule.branch.name+\
                         '%0a'+schedule.branch.location+\
                         '%0aDoctor : '+schedule.doctor.name+\
                         '%0aTime : '+str(start)+' - '+str(end)
        whatsappbtn += messagestring
        context = {
           
        "is_book" : True,
        "schedule":schedule,
        "whatsappbtn":whatsappbtn,
        }
        
        return render(request, 'web/book.html',context)
    

    context = {
        "is_book" : True,
        "schedule":schedule,
        
    }
    return render(request, 'web/book.html',context)

