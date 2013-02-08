__author__ = 'Zhou Guangwen'
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-rss-plugin",
    version="0.0.1",
    author="Guangwen Zhou",
    author_email="zgwmike@hotmail.com",
    description=("A Django CMS plugin to show django-rss-plugin."),
    license="BSD",
    keywords="django cms plugin django-rss-plugin",
    url="http://github.com/zgwmike/django-rss-plugin",
    packages=["rssplugin"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Framework :: Django",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License"
    ],
    requires=['feedparser', 'django-cms'],
    download_url='https://github.com/zgwmike/django-rss-plugin/archive/master.zip',
    long_description=read("README.rst")
)