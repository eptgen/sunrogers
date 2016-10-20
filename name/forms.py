
from django import forms

# Put your forms here, yo.

class NameForm(forms.Form):
	name = forms.CharField(label="Name: ", max_length=50)
	email = forms.CharField(label="Email: ", max_length=40)
	age = forms.IntegerField(label="Age: ")