from django.db import models

class Student(models.Model):
    firstname=models.CharField(max_length=260)
    lastname=models.CharField(max_length=260)
    roll=models.IntegerField()

    def __str__(self):
        return self.firstname+"\t"+self.lastname
