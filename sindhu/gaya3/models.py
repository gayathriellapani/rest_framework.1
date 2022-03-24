from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
    address=models.TextField()
    phoneno:models.IntegerField()
    def __str__(self):
        return self.name
# Create your models here.
