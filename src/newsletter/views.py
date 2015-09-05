from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm

def home(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)
	#if request.user.is_authenticated():
		#title = "Logged as %s" %(request.user)
	
	context = {
		"template_title": title,
		"form": form
	}

	if form.is_valid():
		#print request.POST['email']
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New Full Name"
		instance.full_name = full_name
		form.save()
		'''if not instance.full_name:
			instance.full_name = "Daniel Form"
			instance.save()'''
		context = {
			"template_title": "Thank You"
		}

	
	return render(request, "base.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key, value in form.cleaned_data.iteritems():
		#		print key, value
			#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")

		subject = "Site contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'daniel.albuquerque17@hotmail.com']
		contact_message = "%s: %s via %s"%(
			form_full_name, 
			form_message, 
			form_email)

		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
		

	context = {
		'form': form
	}
	return render(request, "forms.html", context)