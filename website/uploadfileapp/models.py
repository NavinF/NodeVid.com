from django.db import models
import subprocess
from threading import Thread
import os, time

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

    def save(self):
        def helper(self):
            p = subprocess.Popen(['sudo', 'docker', 'run', '--net=host', '-v', os.getcwd()+':/srv/webtorrent', '2cc2a9146aaf',],stdout=subprocess.PIPE)
            while True:
                nextline = p.stdout.read(1)
                print(nextline,'  hell')


        thread = Thread(target = helper, args=(self,))
        thread.start()

        return super(Video, self).save()
