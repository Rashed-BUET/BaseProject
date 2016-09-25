from django import forms





class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name')
	email = forms.EmailField()
	age = forms.IntegerField()
