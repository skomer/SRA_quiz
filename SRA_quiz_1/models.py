from django.db import models

# Create your models here.


class Entry(models.Model):
	email = models.CharField(max_length=200)
	q1_answer = models.CharField(max_length=1000)
	q2_answer = models.CharField(max_length=1000)
	q3_answer = models.CharField(max_length=1000)
	status = models.BooleanField()

	def save():
		return

	def submit():
		return

	def edit():
		return