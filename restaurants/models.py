from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	image = models.ImageField(null=True)

	def __str__(self):
		return self.name

class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant, default =1, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=4, decimal_places =3)
	
	def __str__(self):
		return self.name

class Favorite(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	
	
	def __str__(self):
		return self.name

class Favorite_item(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	
	def __str__(self):
		return self.name
