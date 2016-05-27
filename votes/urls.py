from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import NextVoteView, VoteView


urlpatterns = [
    url(r'^nextvote/$',
        login_required(NextVoteView.as_view()),
        name='next-vote'),
    url(r'^vote/$',
        login_required(VoteView.as_view()),
        name='vote'),
]
