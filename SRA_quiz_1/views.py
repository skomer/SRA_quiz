from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return render(request, 'SRA_quiz_1/index.html', {})

# Create your views here.

