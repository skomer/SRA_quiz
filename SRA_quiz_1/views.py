from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.conf import settings
from models import Entry




def index(request):
	return render(request, 'SRA_quiz_1/index.html', {})

# Create your views here.



def add_answer(request):
	q1_answer = request.POST.get('q1_answer_id')
	# status = False
	status = False
	new_answer_entry = Entry()
	new_answer_entry.q1_answer = q1_answer
	new_answer_entry.status = status
	new_answer_entry.save()
	return render(request, 'SRA_quiz_1/answer_added.html', { 'new_answer_entry' : "You added an answer. yay unicorns"})


def user_dash(request):
	
	return render(request, 'SRA_quiz_1/user_dash.html', {})









def view_image(request):
	return HttpResponse('index')


def save_text_and_close_image(request):
	return HttpResponse('index')


def cancel_and_close_image(request):
	return HttpResponse('index')


def submit_all_answers(request):
	return HttpResponse('index')