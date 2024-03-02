from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    projects = models.Project.objects.all()[:3]
    return render(request, "index.html", {'title': 'Jon Bancroft',
                                          'projects': projects})


def all_projects(request):
    projects = models.Project.objects.all()
    return render(request, "projects.html", {'title': 'Projects',
                                             'projects': projects})


def project(request, project_id):
    project = models.Project.objects.filter(id=project_id).first()
    return render(request, "project.html", {'title': project.name,
                                            'project': project})


def resume(request):
    return render(request, "resume.html", {'title': 'Resume'})


def about(request):
    return render(request, "about.html", {'title': 'About me :-)'})


def contacts(request):
    return render(request, "contacts.html", {'title': 'Contacts'})


def error_404(request, exception=None):
    return render(request, "404.html", status=404)
