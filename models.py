from django.db import models
from django.urls import reverse


# Create your models here.
class registration(models.Model):
	# username = models.CharField(max_length=200, blank=False, null=False),
	# fname = models.CharField(max_length=100, blank=False),
	# lname = models.CharField(max_length=100, blank=False),
	# email = models.EmailField(max_length=300, blank=False, null=False), 
	# pass1  = models.CharField(max_length=200, blank=False),
	# pass2 = models.CharField(max_length=200, blank=False)

	username = models.TextField()
	fname = models.TextField()
	lname = models.TextField()
	email = models.TextField()
	pass1 = models.TextField()


	def get_absolute_url(self):
		return reverse("authentication:list", kwargs={"id":self.id})

