from django.conf.urls import url, include
from .views import About, edit_about



urlpatterns = [
    url(r'^$', About, name='about'),
    url(r'^(?P<pk>\d+)/edit/$', edit_about, name='edit_about')
    
]