from django.shortcuts import render
from django.http import HttpResponse
from HalfFull.forms import UserForm

from django.contrib.auth import authenticate, login 
from django.http import HttpResponse 
from django.urls import reverse 
from django.shortcuts import redirect
# Create your views here.

def home(request):
    context_dict = {}
    return render(request, 'HalfFull/home.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'HalfFull/about.html', context=context_dict)

def contact(request):
    context_dict = {}
    return render(request, 'HalfFull/contact.html', context=context_dict)

def login(request):
    context_dict = {}
    return render(request, 'HalfFull/login.html', context=context_dict)

def signup(request):
    registered=False
    
    if request.method == 'POST':
    
        user_form = UserForm(request.POST)

    
        if user_form.is_valid(): 
            user = user_form.save() 
            user.set_password(user.password)
            user.save()
        

            profile.user = user
        
            
            
            
            profile.save()
        
            registered=True
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        
    return render(request, 'HalfFull/signup.html', context = {'user_form': user_form, 'registered': registered})

def userpage(request):
    context_dict = {}
    return render(request, 'HalfFull/userpage.html', context=context_dict)

def make_a_crawl(request):
    context_dict = {}
    return render(request, 'HalfFull/make_a_crawl.html', context=context_dict)

def pub_list(request):
    context_dict = {}
    return render(request, 'HalfFull/pub_list.html', context=context_dict)
    

