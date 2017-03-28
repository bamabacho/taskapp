from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Task(models.Model):
	task_name = models.CharField(max_length=255)
	task_details = models.TextField(max_length=1500)
	created_date = models.DateTimeField( default = timezone.now)
	finished_date = models.DateTimeField(blank=True, null=True)
	project_field = models.CharField(max_length=255)
	completed = models.BooleanField()

	def publish(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.task_name



class Board(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(max_length=1500)
	created_date = models.DateTimeField(default = timezone.now)
	board_task = models.ForeignKey(Task, blank=True, null=True)

	def publish(self):
		self.save()







