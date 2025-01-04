from django.db import models

# Create your models here.
class contact_master(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30,primary_key=True)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.name