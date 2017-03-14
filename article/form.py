from django import forms
class ArticleForm(forms.Form):
	title = forms.CharField(required = True)
	content = forms.CharField(widget=forms.Textarea)
	user = forms.CharField(required = True)

class SearchForm(forms.Form):
	title = forms.CharField(required = True)
