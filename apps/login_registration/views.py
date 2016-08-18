from django.shortcuts import render, redirect
from django.contrib import messages
from models import User


# Create your views here.
def index(request):

	return render(request, 'login_registration/index.html')

def success(request):

	return render(request, 'login_registration/success.html')

def register(request):
	if request.method == 'POST':
		result = User.userManager.validateRegistration(request)
	#result is a tuple
	#It will hold a boolean, and the user we just created
	if result[0] == False:
		print 'No user created'
		#result[1] is the errorList
		print_messages(request, result[1])
		print result[1]
		return redirect('/')

	user = result[1]
	request.session['user'] = {
		'id': user.id,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		'method': 'registered'
	}
	return redirect('/success')

def userLogin(request, user):
	request.session['user'] = {
		'id': user.id,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email
	}
	return redirect(request, 'login_registration/success.html')

def login(request):
	if request.method == 'POST':
		result = User.userManager.validateLogin(request)
	#result is a tuple
	#It will hold a boolean, and the user we just fetched
	if result[0] == False:
		print "No user found"
		print result[1]
		print_messages(request, result[1])
		return redirect('/')

	user = result[1]
	request.session['user'] = {
		'id': user.id,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		'method': 'logged in'
	}

	return redirect('/success')

def logout(request):
	request.session.clear()
	return redirect('/')

def print_messages(request, message_list):
	for message in message_list:
		messages.add_message(request, messages.INFO, message)

