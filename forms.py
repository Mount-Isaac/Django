from django import forms
from .models import registration

class ModelRegistration(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput)
	fname = forms.CharField(widget=forms.TextInput)
	lname = forms.CharField(widget=forms.TextInput)
	email = forms.CharField(widget=forms.EmailInput)
	pass1 = forms.CharField(widget=forms.PasswordInput)
	pass2 = forms.CharField(widget=forms.PasswordInput)




	class Meta:
		model = registration
		fields = '__all__'

	def clean_pass2(self):
		pass1 = self.cleaned_data
		pass2 = self.cleaned_data
		if pass1 != pass2:
			raise forms.ValidationError('passwords should match')
		return pass1

