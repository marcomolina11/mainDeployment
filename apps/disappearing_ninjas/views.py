from django.shortcuts import render, redirect

# Create your views here.
def index(request):

	return render(request, 'disappearing_ninjas/index.html')

def allNinjas(request):
	return render(request, 'disappearing_ninjas/ninjas.html')

def showNinjas(request, color):
	
	print color


	context = {
		'color': color
	}
	
	return render(request, 'disappearing_ninjas/ninjas.html', context)
