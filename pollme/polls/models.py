from django.db import models

class Poll(models.Model):
    text = models.CharField(max_length=255)
    pub_date = models.DateField()
