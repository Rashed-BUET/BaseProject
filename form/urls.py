from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^getname/$', views.get_name, name = 'get_name'),
	
]