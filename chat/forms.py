
from django import forms

# Put your forms here, yo.

class ChatForm(forms.Form):
	title = forms.CharField(max_length=100)
	body = forms.CharField(max_length=1000)
	
class PostForm(forms.Form):
	body = forms.CharField(max_length=1000)









































