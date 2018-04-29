from django.db import models


# Create your models here.
from django.urls import reverse


class Video(models.Model):

    #the variable to take the inputs
    video_name = models.CharField(max_length=100)
    magnet_uri= models.CharField(max_length=100)
    video_file = models.FileField()

    # on submit click on the user entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('uploadfileapp:home')
