from django.db import models

class SignUp(models.Model):
	email 	  = models.EmailField()
	full_name = models.CharField(max_length=100, blank=True, null=True,default='')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	udpated   = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email