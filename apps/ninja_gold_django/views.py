from django.shortcuts import render, redirect
import random
import datetime
# Create your views here.
def index(request):

	if 'total' in request.session:
		print "there is already a session"
	else:
		print "new session started"
		request.session['total'] = 0
		request.session['message'] = []


	return render(request, 'ninja_gold_django/index.html')

def process(request):
	if request.method == 'POST':
		if request.POST['building'] == 'farm':
			print "farm button pressed"
			date = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M:%S %p)")
			amount = random.randint(10,20)
			request.session['total'] += amount
			request.session['message'].append("Earned " + str(amount) + " golds from the farm! " + str(date))
			print request.session['message']
		if request.POST['building'] == 'cave':
			print "cave button pressed"
			date = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M:%S %p)")
			amount = random.randint(5,10)
			request.session['total'] += amount
			request.session['message'].append("Earned " + str(amount) + " golds from the cave! " + str(date))
			print request.session['message']
		if request.POST['building'] == 'house':
			print "house button pressed"
			date = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M:%S %p)")
			amount = random.randint(2,5)
			request.session['total'] += amount
			request.session['message'].append("Earned " + str(amount) + " golds from the house! " + str(date))
			print request.session['message']
		elif request.POST['building'] == 'casino':
			print "casino button pressed"
			luck = random.randint(0,1)
			amount = random.randint(0,50)
			date = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M:%S %p)")
			if luck == 0:
				request.session['total'] -= amount
				request.session['message'].append("Entered a casino and lost " + str(amount) + " golds... Ouch.. " + str(date))
			elif luck == 1:
				request.session['total'] += amount
				request.session['message'].append("Entered a casino and won " + str(amount) + " golds... Yay!.. " + str(date))


		#process the money
	return redirect('/')