from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    mail_id = models.EmailField()
    address = models.TextField(max_length=255)
    department = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    purpose = models.CharField(max_length=100)
    materials_provided = models.CharField(max_length=100)

    def __str__(self):
        return self.name

