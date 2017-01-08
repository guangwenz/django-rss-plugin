=====================
Django CMS RSS Plugin
=====================

Simple plugin to show an RSS feed in your django cms site.

Features
========
* Show specified number of feeds in the page.
* You can choose to open the feed in current window or new window.
* Show any RSS feed you specified, it can be your external RSS url, or your internal RSS relative url like '/myblog/rss'.
* The feed list would be cached for specified time long.
* You can choose the template of your RSS feed or use the default

Usage
=====

**Installation**::

  $ pip install django-rss-plugin

Add rssplugin to your INSTALLED_APPS in Django settings.py file, Like following::

  INSTALLED_APPS=(
  	'rssplugin',
  )

*Django >= 1.7*::

Run django migrate to install plugin database::

  $ python manage.py migrate rssplugin

*Django and South*::

In your settings.py file, set the south migration module::

  SOUTH_MIGRATION_MODULES = {
    'rssplugin': 'rssplugin.south_migrations',
  }

Run south migrate to install plugin database::

  $ python manage.py migrate rssplugin

*Django < 1.7 without South*::

  $ python manage.py syncdb

**template filter**

#. parsed_to_date::

    {% load rss_tags %}
    {{ entry.published_parsed|parsed_to_date|timesince }}

see rss.html for usage examples.

**Notice**, both external link like 'http：//example.com/rss' and internal link like '/blog/rss' are supported.


**Using custom templates**

Use `CMS_RSS_PLUGIN_TEMPLATE = "path_to_your_template.html"` in settings.py to set a custom template, default is rss/rss.html.

If you specify CMS_RSS_PLUGIN_TEMPLATES instead, rssplugin offers authors an optional
choice of custom templates.

Example::

  CMS_RSS_PLUGIN_TEMPLATES = (
      ('short.html', gettext('Short')),
      ('long.html', gettext('Long')),
      ('mailing_list.html', gettext('List Server')),
  )

For a reference of the feed and entry attributes you can use in your templates, have a look at the feedparser dokumentation: https://pythonhosted.org/feedparser/

**Feed timeout**

Use `CMS_RSS_PLUGIN_FEEDPARSER_TIMEOUT = seconds` in settings.py to set a custom socket timeout, default is 60

Online Resources
----------------

* `Code repository`_.

.. _Code repository: https://github.com/zgwmike/django-rss-plugin
