from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=288)
    email=models.CharField(max_length=288)
    address=models.TextField()
    phone=models.IntegerField()




    