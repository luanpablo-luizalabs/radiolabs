import json

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import Http404
from django.views.generic import View, TemplateView, CreateView, DeleteView

from .forms import VideoForm
from .models import Video
from .utils import get_current


class PlayingView(TemplateView):
    template_name = 'videos/playing.html'

    def get_context_data(self, **kwargs):
        context = super(PlayingView, self).get_context_data(**kwargs)
        try:
            context['video'] = get_current()
        except AttributeError:
            context['video'] = None
        return context


class VideoAddView(CreateView):
    http_method_names = ['post', ]
    model = Video
    form_class = VideoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self):
        kwargs = super(VideoAddView, self).get_form_kwargs()
        url = self.request.POST.get('url')
        if url:
            if 'youtube' not in url:
                # just id
                url = 'https://www.youtube.com/watch?v={}'.format(url)
            mutable = kwargs['data']._mutable = True
            kwargs['data']['url'] = url
            kwargs['data']._mutable = mutable
        return kwargs


class VideoDeleteView(DeleteView):
    model = Video
    slug_field = 'video_id'
    slug_url_kwarg = 'video_id'
    success_url = reverse_lazy('videos:playing')

    def get_object(self, queryset=None):
        try:
            return self.model.objects.get(**{
                self.slug_field: self.kwargs.get(self.slug_url_kwarg)
            })
        except self.model.DoesNotExist:
            raise Http404("Object already deleted")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise Http404("Can't delete due to AnonymousUser")
        return super(VideoDeleteView, self).dispatch(request, *args, **kwargs)


class VideoListView(View):
    model = Video

    def get(self, request, *args, **kwargs):
        return HttpResponse(
            json.dumps(list(
                self.model.objects.exclude(pk=getattr(get_current(), 'pk', 0)).values_list(
                    'id', flat=True
                )
            ))
        )
