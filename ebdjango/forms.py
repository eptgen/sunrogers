
from django import forms

class ChristmasForm(forms.Form):
	one = forms.CharField(max_length=50)
	two = forms.CharField(max_length=50)
	three = forms.CharField(max_length=50)