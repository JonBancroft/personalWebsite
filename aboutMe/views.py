from django.shortcuts import render
from django.core.serializers import serialize
from . import models

# Create your views here.
def home(request):
    projects = models.Project.objects.all().order_by("-priority")[:3]
    return render(request, "index.html", {'title': 'Jon Bancroft',
                                          'projects': projects})


def all_projects(request):
    projects = models.Project.objects.all().order_by("-priority")
    return render(request, "projects.html", {'title': 'Projects',
                                             'projects': projects})


def project(request, project_id):
    project = models.Project.objects.filter(id=project_id).first()
    gallery_images = models.GalleryImage.objects.filter(project=project).all()

    return render(request, "project.html", {'title': project.name,
                                            'project': project,
                                            'gallery_images': gallery_images})


def resume(request):
    return render(request, "resume.html", {'title': 'Resume'})


def about(request):
    return render(request, "about.html", {'title': 'About me :-)'})


def contacts(request):
    return render(request, "contacts.html", {'title': 'Contacts'})


def error_404(request, exception=None):
    return render(request, "404.html", status=404)
