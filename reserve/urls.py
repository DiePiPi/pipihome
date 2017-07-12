# urls.py
#dir /apps/

from django.conf.urls import url

from .views import reservehome, nothing_here, tutor

urlpatterns = [
    url(r'^$', reservehome),
    url(r'^(?P<lesson>\w+( +\w+)*)/$', tutor, name='tutor'), #  \w+( +\w+)*  allows words with multiple space
    
    url(r'.*', nothing_here),
]
