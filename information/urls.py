from django.conf.urls import url, include
from.views import info

urlpatterns = [
    url(r'^info/', info, name="info"),
    
    ]