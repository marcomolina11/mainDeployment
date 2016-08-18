from django.shortcuts import render, redirect
from .models import Email 

# Create your views here.
def index(request):

	return render(request, "emailvalidation/index.html")

def validate(request):
	if request.method == 'POST':

		error = Email.emailManager.validate(request.POST['email'])

		if error:
			print "no login. Validation failed"
			return redirect('/')
		else:
			print "successful login"
			return redirect('/success')

	else: 
		return redirect('/')

def success(request):

	emails = Email.objects.all()

	context = {
		'emails':emails
	}

	return render(request, 'emailvalidation/success.html', context)
