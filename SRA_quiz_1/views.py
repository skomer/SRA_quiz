from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.conf import settings
from models import Entry
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.sessions.models import Session
from importlib import import_module



# starting point
def index(request):
	print "index() >>", request
	return render(request, 'SRA_quiz_1/index.html', {})



# vvv checks whether the email address entered already exists in the db, whether the user has already finally submitted their entry, or else creates a new db row for the user
# change this to do this basically:
# try:
# 	model.objects.get(pk=1)
# except model.DoesNotExist:
# 	model.objects.create(pk=1)
# http://stackoverflow.com/questions/17960593/multipleobjectsreturned-with-get-or-create

def check_email(request):
	email = request.POST.get('email')
	if Entry.objects.filter(email=email).exists() == True:
		selection = Entry.objects.get(email=email)
		if selection.status == True:
			render(request, 'SRA_quiz_1/already_submitted.html', {})
		else:
			return user_dash(request, email)
	else:
		return new_entrant(request, email)


def new_entrant(request, email):
	newbie = Entry(email=email)
	newbie.save()
	return user_dash(request, email)



def user_dash(request, email):
	this_user = Entry.objects.get(email=email)
	q1_answer = this_user.q1_answer
	q2_answer = "blahblah"
	q3_answer = "blahblahblah"
	return render(request, 'SRA_quiz_1/user_dash.html', { 'email' : email, 'q1_answer_id' : q1_answer, 'q2_answer_id' : q2_answer, 'q3_answer_id' : q3_answer })




def add_answer(request):
	email = request.POST.get('email_from_form')
	q1_answer = request.POST.get('q1_answer_id')
	q2_answer = request.POST.get('q2_answer_id')
	q3_answer = request.POST.get('q3_answer_id')
	# q4_answer = request.POST.get('q4_answer_id')
	# q5_answer = request.POST.get('q5_answer_id')
	# q6_answer = request.POST.get('q6_answer_id')
	new_answer_entry = Entry.objects.get(email=email)
	new_answer_entry.q1_answer = q1_answer
	new_answer_entry.q2_answer = q2_answer
	new_answer_entry.q3_answer = q3_answer
	# new_answer_entry.q4_answer = q4_answer
	# new_answer_entry.q5_answer = q5_answer
	# new_answer_entry.q6_answer = q6_answer
	new_answer_entry.save()
	# use HttpResponseRedirect here, as the view has successfully dealt with POST data.
	# but first need to fix the include urls thing, so that the urls will correctly deal with this line:
	# return HttpResponseRedirect(reverse('SRA_quiz_1:user_dash'))
	return render(request, 'SRA_quiz_1/answer_added.html', { 'new_answer_entry' : "You added an answer. yay unicorns"})




def view_image(request):
	return HttpResponse('index')


def save_text(request):
	# use HttpResponseRedirect here?
	return HttpResponse('index')


def cancel_and_close_image(request):
	return HttpResponse('index')


def submit_all_answers(request):
	# use HttpResponseRedirect here?
	return HttpResponse('index')




