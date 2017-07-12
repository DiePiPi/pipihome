# views.py
#dir /reserve/

from django.shortcuts import get_list_or_404, get_object_or_404, render

from django.http import HttpResponse,HttpResponseRedirect

from .models import post, tutorial

# Create your views here.

def nothing_here(request):
	return render(request, '404.html')
	
def reservehome(request):
	if 'language' in request.COOKIES:
		pref_lan = request.COOKIES['language']
	else:
		pref_lan = 'en'
		
	tu = post.objects.filter(post_type = 'tu')
	fx = post.objects.filter(post_type = 'fx')
	
	# render cannot do set_cookie in return function at the same time :/
	response = render(request, 'reservehome.html', {'tu':tu, 'fx':fx})
	response.set_cookie(key='language', value=pref_lan)
	
	return response

def tutor(request, lesson='Setting'):
	print(lesson)
	#kwargs = {'{0}__{1}'.format('title', 'exact'): lesson}
	pos = get_object_or_404(post, title = lesson)
	steps = tutorial.objects.filter(forpost = pos.id)
	
	return render(request, 'tutorial.html', {'post':pos, 'steps':steps})
