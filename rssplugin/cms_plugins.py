__author__ = 'Zhou Guangwen'

import logging

from rssplugin.models import RSSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.core.cache import cache
from django.utils.translation import ugettext as _
import feedparser


class PlanetPlugin(CMSPluginBase):
    model = RSSPlugin
    name = _("RSS Plugin")
    render_template = "rss/rss.html"
    admin_preview = False

    def render(self, context, instance, placeholder):
        feed = cache.get(instance.rss_url)
        if not feed:
            url = self._build_feed_url(context, instance.rss_url)
            feed = feedparser.parse(url)
            if 'bozo_exception' in feed:
                logging.warning('Error parsing feed %s.  Error: %s' % (instance.rss_url, feed['bozo_exception']))
                del feed['bozo_exception']  # have to delete to avoid pickling error in cache
            cache.set(instance.rss_url, feed, instance.cache_time)
        context.update({"instance": instance,
                        "feed": feed})
        return context

    def _build_feed_url(self, context, rss_url):
        request = context.get('request')
        if not ''.startswith('http') and request:
            rss_url = request.build_absolute_uri(rss_url)
        return rss_url


plugin_pool.register_plugin(PlanetPlugin)
