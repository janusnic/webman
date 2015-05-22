from django.conf.urls import include, url
from blog import views

urlpatterns = [
    # Examples:
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^categories/(?P<categoryslug>.*)/$', 'blog.views.category'),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
   
]
