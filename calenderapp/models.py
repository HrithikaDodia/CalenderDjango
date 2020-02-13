from django.db import models

# Create your models here.

class ScheduleEvent(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
    	return self.title