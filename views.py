from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import View
from .forms import ModelRegistration
from .models import registration 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings

# Create your views here.


class class_signup(View):
	template_name = 'authentication/account_signup.html'

	def get(self, request, *args, **Kwargs):
		try:
		# #queryset = registration.objects.all()
		# #obj = get_object_or_404(registration, id=1)
		# form = ModelRegistration()
		# context = {"form": form}

			return render(request, self.template_name, {})
		except ValueError:
			return render(request, self.template_name, {})

	def post(self, request, *args, **Kwargs):
		try:
			username = request.POST['username']
			fname = request.POST['fname']
			lname = request.POST['lname']
			email = request.POST['email']
			pass1 = request.POST['pass1']
			pass2 = request.POST['pass2']

			#print(dir(User.objects))
			if User.objects.filter(username=username):
				messages.error(request, "username exists")
				return redirect('/signup/')
				#return render(request, self.template_name, {})

			if User.objects.filter(email=email):
				messages.error(request, "Email exists")
				return redirect('/signin/')

			if pass1 != pass2:
				messages.error(request,'passwords did not match')
				return redirect('/signup/')
				#return render(request, self.template_name, {})

			my_user = User.objects.create_user(username, email, pass1)
			my_user.first_name = fname
			my_user.last_name = lname

			my_user.save()
			messages.success(request,'Account created successfully')
			return redirect('/signin/')
		except Exception:
			return redirect('/signup/')

class class_signin(View):
	template_name = 'authentication/account_signin.html'

	def queryset(self):
		return User.objects.all()

	def get(self, request, *args, **Kwargs):
		context = {"objects":self.queryset()}
		return render(request, self.template_name, context)


	def post(self, request, *args, **Kwargs):
		username = request.POST['username']
		pass1 = request.POST['pass1']
		#print(dir(User.objects.all.order_by('username')))

		user = authenticate(username=username, password=pass1) #returns a None response if the user is not authenticated
		#print(user)
		if user is not None:
			login(request, user)
			fname = user.first_name
			context = {"fname":fname} 
			#return redirect('../')
			return render(request, 'authentication/account_home.html', context)
		else:
			messages.error(request, 'Bad credentials')
			return redirect('/signin/')



class class_home(View):
	template_name = 'authentication/account_home.html'


	def get(self, request, *args, **Kwargs):
		return render(request, self.template_name, {})

class class_signout(View):

	def get(self, request, *args, **Kwargs):
		#return redirect('../')
		logout(request)
		messages.success(request, 'Logged out successfully')
		return redirect('authentication:home')

class class_userslist(View):
	template_name = 'authentication/account_list.html'
	def get(self, request, *args, **Kwargs):
		obj = get_list_or_404(registration)
		context = {"objects":obj}

		return render(request, self.template_name, context)

def error_404_view(request, exception):
	return render(request, 'authentication/404.html')
