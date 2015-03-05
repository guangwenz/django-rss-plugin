__author__ = 'Zhou Guangwen'

import logging

from rssplugin.models import RSSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.core.cache import cache
from django.utils.translation import ugettext as _
import feedparser

from django.conf import settings
rss_render_template = getattr(settings, 'CMS_RSS_PLUGIN_TEMPLATE', "rss/rss.html")
feedparser_timeout = getattr(settings, 'CMS_RSS_PLUGIN_FEEDPARSER_TIMEOUT', 60)


class PlanetPlugin(CMSPluginBase):
    model = RSSPlugin
    name = _("RSS Plugin")
    render_template = rss_render_template
    admin_preview = False

    def render(self, context, instance, placeholder):
        feed = cache.get(instance.rss_url)
        if not feed:
            url = self._build_feed_url(context, instance.rss_url)
            feed = self._parse_feed(url)
            cache.set(instance.rss_url, feed, instance.cache_time)
        context.update({"instance": instance,
                        "feed": feed})
        return context

    def _build_feed_url(self, context, rss_url):
        request = context.get('request')
        if not ''.startswith('http') and request:
            rss_url = request.build_absolute_uri(rss_url)
        return rss_url

    def _parse_feed(self, rss_url):
        import socket
        default_socket_timeout = socket.getdefaulttimeout()
        try:
            socket.setdefaulttimeout(feedparser_timeout)
            feed = feedparser.parse(rss_url)
            if 'bozo_exception' in feed:
                logging.warning('Error parsing feed %s. Error: %s' % (rss_url, feed['bozo_exception']))
                del feed['bozo_exception'] # have to delete to avoid pickling error in cache
        finally:
            socket.setdefaulttimeout(default_socket_timeout)

        return feed


plugin_pool.register_plugin(PlanetPlugin)
