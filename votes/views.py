from django.db.models import Q
from django.views.generic import TemplateView

from videos.forms import VideoForm
from videos.models import Video


class NextVoteView(TemplateView):                                                
    template_name = 'votes/next_vote.html'

    def get_context_data(self, **kwargs):
        context = super(NextVoteView, self).get_context_data(**kwargs)
        context['video'] = Video.objects.order_by('created').exclude(
            Q(vote__user=self.request.user) |
            Q(user=self.request.user)
        ).first()
        context['form'] = VideoForm()
        return context
