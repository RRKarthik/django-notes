from django.db import models

# Create your models here.
class Notes(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateField(blank=True,null=True)
	body = models.CharField(max_length=250)