from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import random


def index(request):
    labs = Lab.objects.all()
    fields = Field.objects.all() 
    
    best_projects = Project.objects.all().select_related('lab')[:3]
    context = {
        'all_fields': fields,
        'best_projects': best_projects,
    }
    return render(request, 'index.html', context)


def how(request):
    return render(request, 'how.html')


def lab(request, lab_slug):
    lab = Lab.objects.get(slug=lab_slug)
    lab_fields = lab.fields.all()
    context = {
        'lab': lab,
        'lab_fields': lab_fields
    }
    return render(request, 'lab.html', context)
def projects(request, lab_slug, field_slug):
    lab = Lab.objects.get(slug=lab_slug)
    field = Field.objects.get(slug=field_slug)

    projects = Project.objects.filter(lab=lab, field=field)
    context = {
        'projects': projects,
        'lab': lab,
        'field': field,
    }
    return render(request, 'projects.html', context)
def all_projects(request, lab_slug):
    lab = Lab.objects.get(slug=lab_slug)
    projects = Project.objects.filter(lab=lab)
    context = {
        'projects': projects,
        'lab': lab,
    }
    return render(request, 'all_projects.html', context)

def project(request, lab_slug, field_slug, project_slug):
    lab = Lab.objects.get(slug=lab_slug)
    field = Field.objects.get(slug=field_slug)
    project = Project.objects.get(slug=project_slug)
    context = {
        'lab': lab,
        'field': field,
        'project': project,
    }
    return render(request, 'project.html', context)


def about(request):
    labs = Lab.objects.all()
    all_fields = Field.objects.all()
    context = {
        'labs': labs,
        'all_fields': random.sample(list(all_fields), 6)
    }
    return render(request, 'about.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def contact_form(request):
    if request.method == 'POST':
        Application.objects.create(full_name=request.POST['fullname'],
                                   email=request.POST['email'],
                                   phone=request.POST['phone'],
                                   topic=request.POST['subject'],
                                   message=request.POST['message'])
    return redirect('contacts')

def mailing_form(request):
    if request.method == 'POST':
        Mailing.objects.create(email=request.POST['email'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))