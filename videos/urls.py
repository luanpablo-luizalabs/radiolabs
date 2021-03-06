from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import PlayingView, VideoDeleteView, VideoAddView, VideoListView


urlpatterns = [
    url(r'^playing/$', PlayingView.as_view(), name='playing'),

    url(r'^add/$', login_required(VideoAddView.as_view()), name='add'),
    url(r'^list/$', login_required(VideoListView.as_view()), name='list'),
    url(r'^delete/(?P<video_id>[\w-]+)/$',
        VideoDeleteView.as_view(),
        name='delete'),
]
