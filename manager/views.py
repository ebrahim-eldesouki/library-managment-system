from asyncio.windows_events import NULL
from multiprocessing import context
from turtle import st
from django.shortcuts import render, redirect
from .models import student
from .models import books
from .models import mester
from django.http import HttpResponseRedirect
from .form import *
from django.contrib.auth import login,logout,authenticate
import sys
from django.contrib import messages

# Create your views here.
def listbooks(req):
    context={'book':books.objects.filter(borrowed=False)}
    return render(req,'listbooks.html',context)

def listusers(req):
    context={'students':student.objects.all()}
    return render(req,'listusers.html',context)



def update(req,id):
    train=books.objects.get(id=id)
    form=newbook(instance=train)
    if(req.method=='POST'):
       f=newbook(req.POST,instance=train)
       if(f.is_valid()):
          f.save()
          return HttpResponseRedirect('/listbooks')
    context3={'form':form}
    return render(req,'updatebook.html',context3)
    

def home(req):
    return render(req,'home.html',{'msg':"home"})


def search(req):
    search=student.objects.all()
    title=None
    if 'search' in req.GET:
        title=req.GET['search']
        if title:
            search= student.objects.get(id__icontains=title)
    context={'msg':search}
    return render(req,'search.html',context)


def infostd(req,id):
    
    context5={'msg':student.objects.get(id=id)}
    return render(req,'infostd.html',context5)

def adminlogin(req):
    context={}
    if(req.method=='POST'):
        usern=req.POST['Username']
        passw=req.POST['Password']
        try:
            #0,1...n xqueryy[obj0,...objn]
            obj=mester.objects.filter(username=usern,password=passw)
            objauthuser=authenticate(username=usern,password=passw)
           
            if(len(obj)>0 and objauthuser is not None ):
                req.session['userid']=obj[0].id
                req.session['username']=obj[0].username
                req.session['isadmin']=obj[0].isadmin
                print(obj[0].id)
                login(req,objauthuser)
                return HttpResponseRedirect('/')
            else:
                context['msg']='invalid user name or password'
        except:
            context['msg'] = sys.exc_info()[1]
         

    return render(req,'login.html',context)


def adminlogout (req):
    req.session.clear()
    req.session.flush()
    logout(req)
   
    return redirect('/adminlogin')

def prof(req):
    context={'user':mester.objects.all()}
    
    return render(req,'prof.html',context)


def updatepass (req,id):
    
    train=mester.objects.get(id=id)
    form=newpass(instance=train)
    if(req.method=='POST'):
       f=newpass(req.POST,instance=train)
       if(f.is_valid()):
          f.save()
          return HttpResponseRedirect('/prof')
    context3={'form':form}
    return render(req,'update.html',context3)

def addbook (req):
    form=newbook()
    context1={}
    if(req.method=='POST'):
       form=newbook(req.POST)
       if(form.is_valid()):
          form.save()
          return HttpResponseRedirect('/listbooks')
    context1['form']=form  
    print(req.POST)  
    return render(req, 'addbook.html',context1)


def delete(req,id):

    books.objects.get(id=id).delete()
    return HttpResponseRedirect('/listbooks')




def deletestd(req,id):

    student.objects.get(id=id).delete()
    return HttpResponseRedirect('/listusers')




def updatestd(req,id):
    train=student.objects.get(id=id)
    form=newstd(instance=train)
    if(req.method=='POST'):
       f=newstd(req.POST,instance=train)
       if(f.is_valid()):
          f.save()
          return HttpResponseRedirect('/listusers')
    context3={'form':form}
    return render(req,'updatestd.html',context3)







def addstd (req):
    form=newstd()
    context1={}
    if(req.method=='POST'):
       form=newstd(req.POST)
       if(form.is_valid()):
          form.save()
          return HttpResponseRedirect('/listusers')
    context1['form']=form    
    return render(req, 'addstd.html',context1)



def stdlogin(req):
    context={}
    if(req.method=='POST'):
        usern=req.POST['Username']
        passw=req.POST['Password']
        try:
            #0,1...n xqueryy[obj0,...objn]
            obj1=student.objects.filter(username=usern,password=passw)
           
            if(len(obj1)>0 ):
                req.session['id']=obj1[0].id
                req.session['name']=obj1[0].username
                
                print(req.session)
                
                return HttpResponseRedirect('/')
            else:
                context['msg']='invalid user name or password'
        except:
            context['msg'] = sys.exc_info()[1]
         

    return render(req,'stdlogin.html',context)


def stdlogout(req):
    req.session.clear()
    req.session.flush()
    return redirect('/stdlogin')

def bookborrow (req,id):
    train=books.objects.get(id=id)
    form=borrowbook(instance=train)
    if(req.method=='POST'):
       f=borrowbook(req.POST,instance=train)
       if(f.is_valid()):
          f.save()
          return HttpResponseRedirect('/listbooks')
    context3={'form':form}

    return render(req,'borrow.html',context3)


def listborrow(req):
    context={'books':books.objects.filter(borrowed=True).values}
    return render(req,'listborrow.html',context)

def ret (req,id):
    f=books.objects.filter(id=id).update(borrowed=False ,deadline='' ,std_id="")
 
    return HttpResponseRedirect('/stdbooks')

def stdbooks(req,):
    context={'my': books.objects.filter(std_id = req.session['id'] , )}
    return render(req ,'stdbooks.html',context) 








def regist (req):
      if req.method == 'POST':
        obj = student()
        obj.username = req.POST['name']
        obj.password = req.POST['password']
        obj.age = req.POST['age']
        obj.gender = req.POST['gender']
        obj.email = req.POST['email']
        obj.save()
        return redirect('/')
      return render(req, 'reg.html')

def stdprof(req):
    context={'msg':student.objects.get(id=req.session['id'])}
    return render(req,'stdprof.html',context)



def updateprof(req,id):
    train=student.objects.get(id=id)
    form=newstd(instance=train)
    if(req.method=='POST'):
       f=newstd(req.POST,instance=train)
       if(f.is_valid()):
          f.save()
          return HttpResponseRedirect('/stdprof')
    context3={'form':form}
    return render(req,'updateprof.html',context3)

















