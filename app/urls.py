from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^get_range_data$', views.get_range_data, name='get_range_data'),
]
