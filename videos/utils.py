from django.db.models import Sum

from .models import Video


def get_current():
    qs = Video.objects.order_by('created').annotate(
        votes=Sum('vote__vote')
    )

    next_video = None
    for obj in qs:
        if obj.votes is None:
            obj.votes = 0

        if not next_video:
            next_video = obj
        elif next_video.votes < obj.votes:
            next_video = obj
    if not next_video.playing:
        next_video.playing = True
        next_video.save()
    return next_video
