from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    return render(request, "index.html", {'title': 'Jon Bancroft'})


def all_projects(request):
    projects = models.Project.objects.all()
    return render(request, "projects.html", {'title': 'Projects',
                                             'projects': projects})


# TODO: update this
def project(request, project_id):
    return render(request, "projects.html", {'title': ''})


def resume(request):
    return render(request, "resume.html", {'title': 'Resume'})


def about(request):
    return render(request, "about.html", {'title': 'About me :-)'})


def contacts(request):
    return render(request, "contacts.html", {'title': 'Contacts'})


def error_404(request, exception=None):
    return render(request, "404.html", status=404)
