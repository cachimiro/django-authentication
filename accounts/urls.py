from django.conf.urls import url, include
from accounts.views import logout, login, register, profile, form_for_editing_index
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^new/$', form_for_editing_index, name='new_index'),
    url(r'^(?P<pk>\d+)/amend/$', form_for_editing_index, name='edit_index'),

    ]