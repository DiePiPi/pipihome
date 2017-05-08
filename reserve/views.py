# views.py
#dir /reserve/

from django.shortcuts import get_list_or_404, get_object_or_404, render

from django.http import HttpResponse,HttpResponseRedirect

from .models import post, tutorial

# Create your views here.

def nothing_here(request):
	return render(request, '404.html')
	
def reservehome(request):
	tu = post.objects.filter(post_type = 'tu')
	fx = post.objects.filter(post_type = 'fx')
	return render(request, 'reservehome.html', {'tu':tu, 'fx':fx})

def tutor(request, lesson='Setting'):
	#kwargs = {'{0}__{1}'.format('title', 'exact'): lesson}
	pos = get_object_or_404(post, title = lesson)
	steps = tutorial.objects.filter(forpost = pos.id)
	
	return render(request, 'tutorial.html', {'post':pos, 'steps':steps})
