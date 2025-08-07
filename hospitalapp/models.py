from django.db import models

# Create your models here.
class patient(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.firstname + " " + self.surname

class doctor(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    speciality = models.CharField(max_length=100)
    maritalstatus = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    birthday = models.DateField()
    appointmenttime = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

class ward(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    department = models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name + "  " + self.department + "  " + self.description

class Appoint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
       return self.name

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

