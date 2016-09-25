from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^getname/$', views.get_name, name = 'get_name'),
	url(r'^signup/$', views.sign_up, name = 'sign_up'),
	
]