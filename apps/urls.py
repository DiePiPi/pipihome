# urls.py
#dir /apps/

from django.conf.urls import url

from .views import appshome, nothing_here

urlpatterns = [
    url(r'^$', appshome),
    
    url(r'.*', nothing_here),
]
