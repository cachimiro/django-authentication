from django.conf.urls import url, include
from .views import all_products, create_or_edit_product



urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^new/$', create_or_edit_product, name='new_product'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_product, name='edit_product'),
]