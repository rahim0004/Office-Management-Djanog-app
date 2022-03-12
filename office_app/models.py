from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) :
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) :
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(default=0)
    bonus = models.PositiveIntegerField(default=0)
    phone = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"



class StuffInfo(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)

     #additional
     portfolio_site = models.URLField(blank=True)
     profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)


     def __str__(self):
        return self.user.username
    