from django.db import models
from django import forms

# Create your models here.

class Admin:
    pass

class AFile(models.Model):
    name = models.CharField(max_length=200)
    magnet_uri = models.CharField(max_length=1024)
    file_description = models.CharField(max_length=200)
    file = models.FileField(upload_to='files')


    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
