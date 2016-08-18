from __future__ import unicode_literals

from django.db import models
import bcrypt, re
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def validateRegistration(self, request):
		errorList = []

		if request.POST['first_name'] < 2 or request.POST['last_name'] < 2:
			errorList.append('Please enter a valid First and Last Name. (more than 2 characters')

		if str.isalpha(str(request.POST['first_name'])) == False or str.isalpha(str(request.POST['last_name'])) == False:
			errorList.append('Please enter a valid First and Last Name. (letters only')
 
		if not EMAIL_REGEX.match(request.POST['email']):
			errorList.append('Please enter a valid email.')

		if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['c_password']:
			errorList.append('Passwords must match and be at least 8 characters')
		
		if len(errorList) > 0:
			return (False, errorList)
		#if it makes it here, there are no errors
		#So we must hash the password and create the user
		pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

		user = self.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=pw_hash)

		return (True, user)

	def validateLogin(self, request):
		user = self.filter(email=request.POST['email'])

		if len(user) == 0:
			return (False, ["Email/password does not match"])

		password = request.POST['password'].encode()
		if bcrypt.hashpw(password, user[0].pw_hash.encode()):
			return (True, user[0])

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pw_hash =  models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	userManager = UserManager()
	objects = models.Manager()
