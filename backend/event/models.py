from django.db import models
from backend import settings

# Create your models here.

#profile of Evaluator
class Event(models.Model):
  Event_id= models.CharField(max_length=4, primary_key=True)
  Event_Name = models.CharField(max_length=50,blank=True)
  Event_des_short = models.CharField(max_length=200,blank=True)
  Event_des_long = models.CharField(max_length=1000,blank=True)
  Event_Head = models.CharField(max_length=50,blank=True)
  Event_Team = models.CharField(max_length=2000,blank=True)
  Contact_Phone_number1 = models.CharField(max_length=50,blank=True)
  Contact_Email1 = models.CharField(max_length=50,blank=True)
  Contact_Phone_number2 = models.CharField(max_length=50,blank=True)
  Contact_Email2 = models.CharField(max_length=50,blank=True)
  Pre_Registered = models.BooleanField(default=False, blank=False)
  Number_Registered = models.IntegerField(default=0, blank=False)
  Space_Location = models.CharField(max_length=10,blank=True)
  Category=models.CharField(max_length=10,blank=True)

  
  
  def __str__(self):
    return f'{self.Event_Name}'
 