from django.db import models
from django.db.models.base import Model

# Create your models here.
class Member(models.Model):
    first_name = models.CharField("first name", default="", max_length=128)
    middle_name = models.CharField("middle name", default="", max_length=128)
    last_name = models.CharField("last name", default="", max_length=128)
    full_name = models.CharField("full name", default="", max_length=512)
    birth_date = models.DateField("birth date")
    register_date = models.DateTimeField("register date")
    years = models.IntegerField(default=0)