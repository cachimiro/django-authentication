from django.conf.urls import url, include
from .views import all_products, create_or_edit_product,  remove_from_products



urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^new/$', create_or_edit_product, name='new_product'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_product, name='edit_product'),
    url(r'^(?P<pk>\d+)/remove/$', remove_from_products, name='remove_from_products'),
]