from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100, min_length=10)
	message = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()


