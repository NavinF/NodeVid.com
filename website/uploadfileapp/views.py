from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import CreateView

from uploadfileapp.models import Video


class HomeView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'video_list'
    template_name = 'uploadfileapp/home_page.html'

    def get_queryset(self):
        return Video.objects.all()


# view for the user entry page
class VideoEntry(CreateView):
    model = Video
    fields = ['video_name', 'video_file']
