from django.conf.urls import include, url
from .import views

urlpatterns = [
    url(r'^$', views.super_list, name='super_list'),

]
