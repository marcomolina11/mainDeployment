from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailManager(models.Manager):
	def validate(self, email):
		print "running validation function"
		error = False

		if len(email) < 1:
			print "Email too short"
			error = True
		if not EMAIL_REGEX.match(email):
			print "Email is not valid"
			error = True

		if error:
			print error
		else:
			new_email = Email.objects.create(email=email)

		return error

class Email(models.Model):
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	emailManager = EmailManager()
	objects = models.Manager()



