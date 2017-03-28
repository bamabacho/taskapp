from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^boards/$', views.board_list, name='board_list'),
	url(r'^$', views.task_list, name='task_list'),
	url(r'^task/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]