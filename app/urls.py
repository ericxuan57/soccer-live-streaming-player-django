from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^get$', views.get, name='get'),
]
