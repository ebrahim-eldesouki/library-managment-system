from tkinter import Widget
from django import forms
from .models import mester ,books ,student
class newpass(forms.ModelForm):
    class Meta:
        model = mester
        fields ='__all__'
        Widget={
            'username': forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
            'password':forms.PasswordInput(attrs={'id':"form1Example1" ,'class':"form-control" })
                   
        }
        
class newbook(forms.ModelForm):
    class Meta:
        model=books
        exclude=['std','deadline','borrowed']
        Widget={
            'name': forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
            'num_papers':forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
            'type':forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" })
        }       
        
        
class newstd(forms.ModelForm):
    class Meta:
        model=student
        exclude=['isadmin']
        Widget={
            'username': forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
            'password':forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
            'gender':forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
             'age':forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
             'email':forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
           
        } 
        

class borrowbook(forms.ModelForm):
    class Meta:
        model=books
        exclude=['name','num_papers','type']
        Widget={
            'std': forms.TextInput(attrs={'id':"form1Example1" ,'class':"form-control" }),
        }       
        