from django.db import models
from django.contrib.auth.models import User


class Intern(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id_number = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="interns",null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id_number})"

