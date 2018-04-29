# /uploadfileapp/
from django.conf.urls import url

from uploadfileapp import views

app_name = 'uploadfileapp'

urlpatterns = [

    # uploadfileapp/
    url(r'^$', views.HomeView.as_view(),name='home' ),

    # uploadifileapp/register
    url(r'^upload/$', views.VideoEntry.as_view(), name='video-entry'),

    url(r'^v/(?P<magnet_uri>[\w\-]+)/$', views.watch, name='video-watch')

]
