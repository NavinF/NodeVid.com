from django.shortcuts import render, get_object_or_404

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

def watch(request, magnet_uri):
    video = get_object_or_404(Video, pk=magnet_uri)
    return render(request, 'uploadfileapp/video.html', {'video': video})
