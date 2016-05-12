from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include('base.urls')),
    url(r'videos/', include('videos.urls', namespace='videos')),
    url(r'votes/', include('votes.urls', namespace='votes')),
]
