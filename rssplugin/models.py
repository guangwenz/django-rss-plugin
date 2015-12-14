from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _


class RSSPlugin(CMSPlugin):
    count = models.IntegerField(default=6)
    title = models.CharField(max_length=200, default="Community News", null=True,
                             help_text=_("If you specified this value, it will replace feed's title"))
    rss_url = models.CharField(max_length=512)
    open_in_new_window = models.BooleanField(default=False)
    cache_time = models.IntegerField(verbose_name=_("Cache time in seconds"))

    def __unicode__(self):
        return self.title
