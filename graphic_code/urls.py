# -*- coding: UTF-8 -*-


from django.conf.urls import url

from . import views

app_name = 'graphic_code'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^barcode/(?P<code>[a-zA-Z0-9]+)/(?P<name>[a-zA-Z0-9]+)$', views.create_barcode, name='create_barcode'),
]
