# views.py
#dir /
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect



# Create your views here.

def nothing_here(request):
	return render(request, '404.html')
	
def home(request):
	return render(request, 'home.html', {'hello': 'Hello!'})
