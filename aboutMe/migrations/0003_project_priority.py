# Generated by Django 5.0.2 on 2024-03-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutMe', '0002_rename_image_project_thumbnail_project_repo_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
