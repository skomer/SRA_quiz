from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.conf import settings
from models import Onemodel
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required



# starting point
def index(request):
	return render(request, 'SRA_quiz_1/index.html', {})



# checks whether the email address entered already exists in the db, whether the user has already finally submitted their entry, or else creates a new db row for the user
def check_email(request):
	email = request.POST.get('email')
	# u = Onemodel.objects.get(email=email)
	if Onemodel.objects.filter(email=email).exists() == True:
		selection = Onemodel.objects.get(email=email)
		if selection.status == 1:
			render(request, 'SRA_quiz_1/already_submitted.html', {})
		else:
			return user_dash(request)
	else:
		return new_entrant(request)


def new_entrant(request):
	email = request.POST.get('email')
	newbie = Onemodel(email=email, status=0)
	newbie.save()
	return user_dash(request)



def add_answer(request):
	q1_answer = request.POST.get('q1_answer_id')
	status = False
	new_answer_entry = Entry()
	new_answer_entry.q1_answer = q1_answer
	new_answer_entry.status = status
	new_answer_entry.save()
	return render(request, 'SRA_quiz_1/answer_added.html', { 'new_answer_entry' : "You added an answer. yay unicorns"})



def user_dash(request):
	q1_answer = "blah"
	q2_answer = "blahblah"
	q3_answer = "blahblahblah"
	return render(request, 'SRA_quiz_1/user_dash.html', { 'q1_answer_id' : q1_answer, 'q2_answer_id' : q2_answer, 'q3_answer_id' : q3_answer })


def view_image(request):
	return HttpResponse('index')


def save_text_and_close_image(request):
	return HttpResponse('index')


def cancel_and_close_image(request):
	return HttpResponse('index')


def submit_all_answers(request):
	return HttpResponse('index')




