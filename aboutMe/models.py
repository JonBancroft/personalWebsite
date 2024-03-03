from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='images/')
    repo_link = models.URLField()


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="images/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
