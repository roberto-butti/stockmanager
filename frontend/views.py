# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def indexAction(request):
	return render(request, 'index.html', {})

def loginAction(request):
	msg = "" # define a message for the user for the login state

	if request.method == 'POST':
		# do the authentication
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				# User is not active
				msg = "Utente non attivo"
		else:
			# Invalid login
			msg = "Login errata"

	# redirect if user is already logged-in
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	# render the view
	return render(request, 'login.html', {"msg": msg})

def registerAction(request):
	return render(request, 'register.html', {})
