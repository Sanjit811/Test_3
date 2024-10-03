from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    E_mail = models.EmailField(max_length=100)
    Phone_Number = models.CharField( max_length=10)
    Description = models.CharField(max_length=500 ,null=True)



    def __str__(self):
        return self.E_mail
    
# create membership model
class Membership(models.Model):
    Plan_ID = models.AutoField(primary_key=True)
    Plan_Name = models.CharField(max_length=150)
    plan_price = models.IntegerField()
    is_Active = models.BooleanField()


    def __str__(self):
        return self.Plan_ID
    

# create Trainer model

class Trainer(models.Model):
    Trainer_ID = models.AutoField(primary_key=True)
    Trainer_Name = models.CharField(max_length=150)
    Trainer_Gender = models.CharField(max_length=15)
    Trainer_Phone = models.CharField(max_length=10)
    Trainer_salary = models.IntegerField()
    Trainer_JoiningDate = models.DateTimeField(auto_now_add=True, blank=True)
    is_Active = models.BooleanField()

    
    def __str__(self):
        return self.Trainer_Name
    

# create enrollment


class Enrollment(models.Model):
    Enrollment_ID = models.AutoField(primary_key=True)
    Enrollment_Full_Name = models.CharField(max_length=100)
    Enrollment_Email = models.EmailField(max_length=100)
    Enrollment_Gender = models.CharField(max_length=100)
    Enrollment_Number = models.CharField(max_length=100)
    Enrollment_DOB = models.CharField(max_length=100)
    Enrollment_Selecte_membership_plan = models.CharField(max_length=100)
    Enrollment_Selected_Trainer = models.CharField(max_length=100)
    Enrollment_Reference = models.CharField(max_length=100)
    Enrollment_Address = models.TextField(max_length=1000 , null=True, blank=True)
    Enrollment_Payment_status = models.CharField(max_length=100 , blank=True , null=True )
    Enrollment_price = models.CharField(max_length=100 , null=True)
    Enrollment_DueDate = models.DateTimeField( blank=True , null=True)
    Enrollment_JoiningDate = models.DateTimeField(auto_now_add=True, blank=True)
    is_Active = models.BooleanField()

     
    def __str__(self):
        return self.Plan_ID
    
# create attendance model

class Attendance(models.Model):
    Attendance_ID = models.AutoField(primary_key=True)
    Selected_date = models.DateTimeField(default=timezone.now)
    phone_Number = models.CharField(max_length=15)
    log_in = models.CharField(max_length=100)
    log_out = models.CharField(max_length=100)
    Selected_workout = models.CharField(max_length=200)
    trained_By = models.CharField(max_length=200)

    def __str__(self):
        return self.Attendance_ID




