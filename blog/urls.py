from django.conf.urls import url
from . import views

urlpatterns = [
    # this is assigning a view called post_list to the url ^S
    url(r'^$', views.post_list, name='post_list'),
]
