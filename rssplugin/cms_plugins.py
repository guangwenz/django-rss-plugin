__author__ = 'Zhou Guangwen'

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
            feed = feedparser.parse(instance.rss_url)
            cache.set(instance.rss_url, feed, instance.cache_time)
        context.update({"instance": instance,
                        "feed": feed})
        return context


plugin_pool.register_plugin(PlanetPlugin)