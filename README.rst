=====================
Django CMS RSS Plugin
=====================

Simple plugin to show a a rss feed in your django cms site.

Features
========
* Show specified number of feeds in the page.
* You can choose to open the feed in current window or new window.
* Show any rss feed you specified, it can be your external rss url, or your internal rss relative url like '/myblog/rss'.
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

Run south migrate to install plugin database::

  $ python manage.py migrate rssplugin

If no south, just run::

  $ python manage.py syncdb

**template filter**

#. parsed_to_date::

    {% load rss_tags %}
    {{ entry.published_parsed|parsed_to_date|timesince }}

see rss.html for usage examples.

**Notice**, both external link like 'http：//example.com/rss' and internal link like '/blog/rss' are supported.


**Using custom template**

Use `CMS_RSS_PLUGIN_TEMPLATE = "path_to_your_template.html"` in settings.py to set a custom template, default is rss/rss.html.


**Feed timeout**

Use `CMS_RSS_PLUGIN_FEEDPARSER_TIMEOUT = seconds` in settings.py to set a custom socket timeout, default is 60

Online Resources
----------------

* `Code repository`_.

.. _Code repository: https://github.com/zgwmike/django-rss-plugin
