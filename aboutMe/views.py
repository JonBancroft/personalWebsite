from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")


def all_projects(request):
    return render(request, "projects.html")


# TODO: update this
def project(request, project_id):
    return render(request, "projects.html")


def resume(request):
    return render(request, "resume.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    return render(request, "contacts.html")


def error_404(request, exception=None):
    return render(request, "404.html", status=404)
