# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Vote(models.Model):
    VOTE_CHOICES = (
        (1, 'upvote'),
        (-1, 'downvote'),
    )
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    video = models.ForeignKey('videos.Video')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'votação'
        verbose_name_plural = u'votações'
        unique_together = ('user', 'video')

    def __unicode__(self):
        return u'{} {}d {}'.format(self.user, self.get_vote_display(),
                                   self.video.title)
