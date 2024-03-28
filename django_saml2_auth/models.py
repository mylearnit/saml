from django.db import models

class Logs(models.Model):
    name = models.CharField(max_length=30, blank=True)
    desc = models.TextField()