from django import forms
class ChatForm(forms.Form):
	user = forms.CharField(required = True)
	content = forms.CharField(widget=forms.Textarea)
	

