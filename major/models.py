from django.db import models

# Create your models here.
class IT(models.Model):
	dept = models.CharField(max_length = 255)
	dept_phone =models.CharField(max_length = 255)
	people =models.CharField(max_length=255)
	teacher =models.CharField(max_length=255)
	a_chaw_sone =models.CharField(max_length = 255)

	def __str__(self):
		return self.dept

class Mech(models.Model):
	dept = models.CharField(max_length = 255)
	dept_phone =models.CharField(max_length = 255)
	people =models.CharField(max_length=255)
	teacher =models.CharField(max_length=255)
	a_chaw_sone =models.CharField(max_length = 255)

	def __str__(self):
		return self.dept

class EC(models.Model):
	dept = models.CharField(max_length = 255)
	dept_phone =models.CharField(max_length = 255)
	people =models.CharField(max_length=255)
	teacher =models.CharField(max_length=255)
	a_chaw_sone =models.CharField(max_length = 255)

	def __str__(self):
		return self.dept