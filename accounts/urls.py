from django.conf.urls import patterns, include, url
urlpatterns = patterns('accounts.views',
    url(r'^$', 'index'),
    url(r'^save_account/$', 'save_account'),
)
