from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        password1 = request.POST['password1']
        number = request.POST['number'] 

        if User.objects.filter(email=email).exists():
            messages.info(request,'Username Already Taken')
            print('username taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=first_name, password= password1, email=email, first_name= first_name, last_name= last_name)
            user.save()
            


            return redirect('login')

    else:
        return render(request,'login/register.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']  
        password = request.POST['password']
        user = User.objects.filter(first_name=name)[0]
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')