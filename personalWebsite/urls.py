"""
URL configuration for personalWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aboutMe import views

from django.conf import settings
from django.conf.urls.static import static

handler404 = 'aboutMe.views.error_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("projects/", views.all_projects),
    path("projects/<int:project_id>/",views.project),
    path("resume/", views.resume),
    path("about/", views.about),
    path("contacts/", views.contacts)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)