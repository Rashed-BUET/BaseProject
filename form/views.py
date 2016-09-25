from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import UserForm

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


def sign_up(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = UserForm();


	return render(request, 'form/sign_up.html',{'form':form})
