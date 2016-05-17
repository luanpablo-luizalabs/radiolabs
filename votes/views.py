from django.db.models import Q
from django.views.generic import TemplateView

from videos.models import Video


class NextVoteView(TemplateView):
    template_name = 'votes/next_vote.html'

    def get_context_data(self, **kwargs):
        context = super(NextVoteView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.order_by('created')[1:]
        return context
