from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/add', views.addCourse),
    url(r'^courses/destroy/(?P<id>\d+)', views.youSure),
    url(r'^courses/nukeIt', views.destroy),
]
