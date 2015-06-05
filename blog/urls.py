from django.conf.urls import include, url
from blog import views

urlpatterns = [
    
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^categories/(?P<categoryslug>.*)/$', 'blog.views.category'),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    url(r'^register/$', 'blog.views.register', name='register'), 
    url(r'^login/$', 'blog.views.ulogin', name='login'),
    url(r'^restricted/', 'blog.views.restricted', name='restricted'),
    url(r'^logout/$', 'blog.views.user_logout', name='logout'),
    url(r"^add_comment/(?P<postslug>.*)/$", "blog.views.add_comment"),
    url(r"^month/(\d+)/(\d+)/$", "blog.views.month"),
    url(r'^pages/(?P<pageslug>.*)/$', 'blog.views.page'),
   
]
