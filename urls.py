from django.urls import path
from .views import (
	class_signup, 
	class_signin, 
	class_signout,
	class_home, 
	class_userslist
	#signup
	)
	
app_name = 'authentication'
urlpatterns = [
	path('', class_home.as_view(), name='home'),
	path('<int:id>/', class_userslist.as_view(), name='list'),
	path('signout/', class_signout.as_view(), name='signout'),
	path('signup/', class_signup.as_view(), name='signup'), 
	path('signin/', class_signin.as_view(), name='signin')
]