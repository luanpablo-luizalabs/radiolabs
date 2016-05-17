from django.views.generic import TemplateView

from videos.forms import VideoForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form_video'] = VideoForm()
        return context
