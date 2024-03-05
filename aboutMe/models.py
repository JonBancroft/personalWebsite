from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    tools = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='images/')
    repo_link = models.URLField()
    priority = models.IntegerField()

    def __str__(self): 
         return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="images/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.image.name
