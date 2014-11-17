from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'test', views.index, name='index')
		)
	
#'^$' has been added in order to represent a blank string
#url(r tacks on the url of the base site like tango.com, if you go to tango.com/ there is nothing next to the / therefore a blank space (or ^$ is sent to urlpatterns which names it 'index')
#index calls the content of index in views.py