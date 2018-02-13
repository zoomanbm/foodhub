from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()

	def __str__(self):
		return self.name

class Detail_Restaurant(models.Model):
	name = models.CharField(max_length=255)
	owner = models.CharField(max_length=255)
	number_employees = models.CharField(max_length=255)
	name_manager = models.CharField(max_length=255)

	def __str__(self):
		return self.name
		