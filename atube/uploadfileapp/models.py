from django.db import models


# Create your models here.
from django.urls import reverse


class User(models.Model):

    #the variable to take the inputs
    user_name = models.CharField(max_length=100)
    user_avatar = models.FileField()

    # on submit click on the user entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('uploadfileapp:home')
