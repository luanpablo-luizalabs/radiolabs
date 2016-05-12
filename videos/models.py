# coding: utf-8
from __future__ import unicode_literals

import logging
import requests

from django.conf import settings
from django.db import models


logger = logging.getLogger('django')


class Video(models.Model):
    url = models.URLField(null=True)
    video_id = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        verbose_name = u'Vídeo'
        verbose_name_plural = u'Vídeos'

    def __unicode__(self):
        return self.title

    def save(self, **kwargs):
        if not self.video_id and self.url:
            self.video_id = self.url.split('=')[1]

        if not self.title:
            try:
                self.title = requests.get(
                    settings.TITLE_URL.format(video_id=self.video_id),
                    timeout=2,
                ).json()['items'][0]['snippet']['title']
            except Exception as e:
                logger.exception(e)
                pass

        super(Video, self).save(**kwargs)
