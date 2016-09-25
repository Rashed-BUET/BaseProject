from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
	class Meta:
		model = User
		exclude = []
		# fields = ['first_name','last_name','email','username','password',]
		# widgets = {
  #       	'password': forms.PasswordInput(),
  #   	}
