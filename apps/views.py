# views.py
#dir /apps/

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect



# Create your views here.

def nothing_here(request):
	return render(request, '404.html')
	
def appshome(request):
	return render(request, 'appshome.html', {'hello': 'Hello!'})

### test area ###

def test(request):
	return render(request, 'testex.html')
