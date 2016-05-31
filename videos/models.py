# coding: utf-8
from __future__ import unicode_literals

import logging
import requests
import urlparse

from django.conf import settings
from django.db import models


logger = logging.getLogger('django')


class Video(models.Model):
    url = models.URLField(null=True)
    video_id = models.CharField(max_length=50, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=512, null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    playing = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Vídeo'
        verbose_name_plural = u'Vídeos'

    def __unicode__(self):
        return self.title or u''

    def save(self, **kwargs):
        if not self.video_id and self.url:
            parsed_url = urlparse.urlsplit(self.url)
            query_str = urlparse.parse_qs(parsed_url.query)
            self.video_id = query_str.get('v', '')[0]

        if not self.title or not self.cover_url:
            try:
                resp_json = requests.get(
                    settings.TITLE_URL.format(video_id=self.video_id),
                    timeout=2,
                ).json()
                snippet = resp_json['items'][0]['snippet']
                self.title = snippet['title']
                self.cover_url = snippet['thumbnails']['medium']['url']
            except Exception as e:
                logger.exception(e)
                pass

        super(Video, self).save(**kwargs)

    @property
    def count_like(self):
        return self.vote_set.filter(vote=1).count()

    @property
    def count_dislike(self):
        return self.vote_set.filter(vote=-1).count()
