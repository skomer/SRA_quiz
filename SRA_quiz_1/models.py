from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Entry(models.Model):
	email = models.CharField(max_length=200, null = True)
	status = models.BooleanField(default=False)
	q1_answer = models.CharField(max_length=1000, null = True)
	q2_answer = models.CharField(max_length=1000, null = True)
	q3_answer = models.CharField(max_length=1000, null = True)

