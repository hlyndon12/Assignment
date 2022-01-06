from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def newsfeed(request):
    posts_list = []
 
    posts = Post.objects.all().order_by('-created_at')
    
    for post in posts:
        posts_list.append(post)
    context = {'posts':posts_list}
    return render(request,'users/newsfeed.html',context)
@login_required(login_url='/login/login')
def createpost(request):
    context ={}
  
    # create object of form
    form = PostForm(request.POST or None, request.FILES or None)
    
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('newsfeed')
  
    context['form']= form
    return render(request,'users/createpost.html',context)