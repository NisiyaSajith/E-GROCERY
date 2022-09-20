from django.db import models
from django.contrib.auth.models import AbstractUser
from master.models import Address, TimeStamp


class CustomUser(AbstractUser):
    pass


class Profile(TimeStamp, models.Model):
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('T', 'TRANSGENDER')
    )
    name = models.CharField(max_length=52)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    age = models.IntegerField()
    qualification = models.CharField(max_length=52)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
