from django.conf.urls import url

from . import views

urlpatterns = [
	# views.py
    url(r'^$', views.index, name='index'),
    url(r'^(?P<idx>\d+)/$', views.testcase_details, name='detail'),
]