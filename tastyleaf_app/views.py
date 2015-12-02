from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from models import *
from forms import *
import random

# Create your views here.
def index(request):
	return render(request, 'tastyleaf_app/index.html')

def getStories(request):
	approvedStories = Story.objects.filter(approved=True)
	storyls = []
	for story in approvedStories:
		storyls.append({'author': story.author, 'question': story.question, 
						'quote': story.quote, 'imgurl': story.imgurl})
	size = min([25, len(storyls)])
	returnls = random.sample(storyls, size)
	return JsonResponse({'ls':storyls, 'size':size})

def submitStory(request):
	if request.method == "POST":
		form = StoryForm(request.POST)
		if form.is_valid():
			new_story = form.save()
			return JsonResponse({'success': True})
		else:
			return JsonResponse({'success': False})

	return HttpResponseRedirect('/')