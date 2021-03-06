from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	email = forms.EmailField()
	full_name = forms.CharField(required=False)
	message = forms.CharField()

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .EDU email address")
		return email

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email','full_name']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .EDU email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		return full_name
