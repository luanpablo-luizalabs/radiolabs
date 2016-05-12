from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import NextVoteView


urlpatterns = [
    url(r'^nextvote/$',
        login_required(NextVoteView.as_view()),
        name='next-vote'),
]
