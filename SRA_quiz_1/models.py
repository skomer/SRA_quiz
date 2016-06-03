from django.db import models

# Create your models here.


class Entry(models.Model):
	email = models.CharField(max_length=200, null = True)
	q1_answer = models.CharField(max_length=1000, null = True)
	q2_answer = models.CharField(max_length=1000, null = True)
	q3_answer = models.CharField(max_length=1000, null = True)
	status = models.BooleanField()

	def __str__(self):
		return self.email


	# def save():
	# 	return

	# def submit():
	# 	return

	# def edit():
	# 	return