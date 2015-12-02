from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from models import *

# Create your views here.
def index(request):
	return render(request, 'tastyleaf_app/index.html')
