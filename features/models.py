from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    interests=models.CharField(max_length=122)
    contact=models.CharField(max_length=12)
    


   