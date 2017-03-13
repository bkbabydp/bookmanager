# -*- coding: UTF-8 -*-


from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.index, name='index')
]
