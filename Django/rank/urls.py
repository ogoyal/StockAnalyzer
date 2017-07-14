from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rank_list/$', views.rank_list, name='rank_list'),
    url(r'^logout$', views.logout_view, name='logout'),

]

