from django.db import models
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from official.forms import BranchForm
from .models import Branch


def index(request):
    branchform = BranchForm(request.POST)
    if request.method == 'POST':
        
        if branchform.is_valid():
           branchform.save()
           

      
        response_data = {
            "status" : "true",
            "title" : "Successfully Submitted",
            "message" : "Updated"
        }
        # else:
        #     print (branchform.errors)
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_index" : True,
            "branchform":branchform,
        }
    return render(request, 'official/index.html',context)
