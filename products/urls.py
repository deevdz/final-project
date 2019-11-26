from django.conf.urls import url, include
from .views import workshops, workshop_detail

urlpatterns = [
    url(r'^$', workshops, name='workshops'),
    url(r'^(?P<slug>[-\w]+)/$', workshop_detail, name='workshop_detail'),
]