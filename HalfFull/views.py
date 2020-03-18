from django.shortcuts import render
from django.http import HttpResponse
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
    context_dict = {}
    return render(request, 'HalfFull/signup.html', context=context_dict)

def userpage(request):
    context_dict = {}
    return render(request, 'HalfFull/userpage.html', context=context_dict)

def make_a_crawl(request):
    context_dict = {}
    return render(request, 'HalfFull/make_a_crawl.html', context=context_dict)

def pub_list(request):
    context_dict = {}
    return render(request, 'HalfFull/pub_list.html', context=context_dict)
