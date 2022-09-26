# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('technical/', views.index_technical, name='index_technical'),
    path('engineer/', views.index_engineer, name='index_engineer'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
