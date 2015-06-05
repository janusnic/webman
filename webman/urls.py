"""webman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
#from django.contrib.flatpages import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    #url(r'^tinymce/', include('tinymce.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    #url(r'', include('django.contrib.flatpages.urls')),
    # url(r'^(?P<url>.*/)$', views.flatpage),
    # url(r'^about/$', views.flatpage, {'url': '/about/'}, name='about'),
]
