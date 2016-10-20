
from django import forms

# Put your forms here, yo.
class ArduinoForm(forms.Form):
	code = forms.IntegerField()
	val = forms.CharField(max_length=20)
	

































