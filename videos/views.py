from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import Http404
from django.views.generic import TemplateView, CreateView, DeleteView

from .forms import VideoForm
from .models import Video


class PlayingView(TemplateView):
    template_name = 'videos/playing.html'

    def get_context_data(self, **kwargs):
        context = super(PlayingView, self).get_context_data(**kwargs)
        context['video'] = Video.objects.order_by('created').first()
        return context


class VideoAddView(CreateView):
    http_method_names = ['post', ]
    model = Video
    form_class = VideoForm
    success_url = reverse_lazy('votes:next-vote')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class VideoDeleteView(DeleteView):
    model = Video
    slug_field = 'video_id'
    slug_url_kwarg = 'video_id'
    success_url = reverse_lazy('videos:playing')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise Http404("Can't delete due to AnonymousUser")
        return super(VideoDeleteView, self).dispatch(request, *args, **kwargs)
