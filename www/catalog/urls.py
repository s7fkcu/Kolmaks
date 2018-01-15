﻿# -*- coding: utf-8 -*-

from django.conf.urls import *

from catalog.views import ProductList, ProductItem

urlpatterns = patterns('catalog.views',
	url(r'^$', ProductList.as_view(), name='catalog_url'),
	url(r'^(?P<slug>[-_\w]+)/$', ProductItem.as_view(), name='product_url'),
)