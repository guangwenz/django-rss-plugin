__author__ = 'Zhou Guangwen'
import os
from setuptools import setup, find_packages

PKG_NAME = 'rssplugin'
VERSION = __import__(PKG_NAME).__version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-rss-plugin",
    version=VERSION,
    author="Guangwen Zhou",
    author_email="zgwmike@hotmail.com",
    description="A Django CMS plugin to show a list of feeds.",
    license="BSD",
    keywords="django cms plugin django-rss-plugin",
    url="http://github.com/zgwmike/django-rss-plugin",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Video :: Display',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    install_requires=[
        'feedparser',
        'Django >= 1.4',
        'django-cms >= 2.3'],
    long_description=read("README.rst") + read("CHANGES.rst"),
    packages = find_packages(),
    include_package_data=True,
    zip_safe=False,
)
