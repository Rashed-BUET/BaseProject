from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm


def index(request):
	return HttpResponse("Hello There!")

def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			HttpResponseRedirect("/thanks/")
	else:
		form = NameForm()
	return render(request, 'form/name.html', {'form': form})				


