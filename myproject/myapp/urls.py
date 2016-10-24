from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello/','myapp.views.hello', name='hello'),
    url(r'^morning/','myapp.views.morning', name='morning'),
    url(r'^reminder/','myapp.views.reminder', name='reminder')
	)