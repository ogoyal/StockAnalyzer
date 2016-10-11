from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rank_list, name='rank_list'),
]

