from django.conf.urls import url, include
from .views import info, info_detail, create_or_edit_info



urlpatterns = [
    url(r'^info/', info, name="info"),
    url(r'^(?P<pk>\d+)/$', info_detail, name='info_detail'),
    url(r'^new/$', create_or_edit_info, name='new_info'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_info, name='edit_info')
    
    ]