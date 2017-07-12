# urls.py
#dir /apps/

from django.conf.urls import url

from .views import appshome, nothing_here
from .views import test

urlpatterns = [
    url(r'^$', appshome),
    url(r'^test', test),
    url(r'.*', nothing_here),
]
