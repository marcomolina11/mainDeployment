from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):

	if 'number' in request.session:
		request.session['number'] += 1
	else:
		request.session['number'] = 1

	return render(request, 'random_word_generator/index.html')

def generate(request):
	print request.method
	if request.method == 'POST':
		word = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
		print word
		request.session['word'] = word
		return redirect('/')

	else: 
		return redirect('/')

