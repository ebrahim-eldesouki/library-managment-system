from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class student (models.Model):
    
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=8,null=False)
    age=models.PositiveIntegerField(null=False)
    gender=models.CharField(null=False)
    email=models.CharField(max_length=50,null=False) 
    isadmin=models.BooleanField(default=False)
    
    def __str__(self):
        
       return  self.username  + str(self.age)   +  self.gender + self.email 
    
class books (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=False)
    num_papers=models.PositiveIntegerField(null=False)
    type=models.CharField(max_length=20,null=False)
    borrowed=models.BooleanField(default=False)
    deadline=models.CharField(max_length=20,null=True)
    std=models.ForeignKey( student ,on_delete=models.CASCADE, null=True)
    def __str__(self):
        
       return  self.name  + str(self.num_papers)   +  self.type
    
  

        








class mester(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=20,null=False)
    isadmin=models.BooleanField(null=False,default= True)
    
    
    def __str__(self):
        
       return  self.username 
      