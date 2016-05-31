from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, View

from videos.models import Video
from .models import Vote


class NextVoteView(TemplateView):
    template_name = 'votes/next_vote.html'

    def get_context_data(self, **kwargs):
        context = super(NextVoteView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.exclude(playing=True)
        return context


class VoteView(View):
    def post(self, request, *args, **kwargs):
        vote = request.POST.get('vote')
        video_id = request.POST.get('video_id')
        try:
            vote = int(vote)
            if vote not in (1, -1):
                raise ValueError
        except ValueError:
            return HttpResponseBadRequest()

        video = get_object_or_404(Video, pk=video_id)

        vote_obj, created = Vote.objects.get_or_create(
            user=request.user,
            video=video,
            defaults={'vote': vote}
        )

        if vote == 1:
            prop = 'count_like'
        else:
            prop = 'count_dislike'

        if not created:
            vote_obj.delete()
            return HttpResponse(str(getattr(video, prop)))
        return HttpResponse(str(getattr(video, prop)))
