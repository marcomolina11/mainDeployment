from django.shortcuts import render
import datetime

# Create your views here.
def index(request):

	date = datetime.datetime.now().strftime("%b %d, %Y")
	time = datetime.datetime.now().strftime("%I:%M %p")
	context = {
	 'date':date,
	 'time':time
	}
	return render(request, 'timedisplay/index.html', context)


