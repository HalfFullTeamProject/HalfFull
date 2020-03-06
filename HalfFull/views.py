from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context_dict = {}
    return render(request, 'HalfFull/home.html', context=context_dict)

def about(request):
    return HttpResponse("This is the about page, <a href='/HalfFull/'>home</a>")

def contact(request):
    return HttpResponse("This is the contact page, <a href='/HalfFull/'>home</a>")

def login(request):
    return HttpResponse("This is the login page, <a href='/HalfFull/'>home</a>")

def signup(request):
    return HttpResponse("This is the signup page, <a href='/HalfFull/'>home</a>")

def userpage(request):
    return HttpResponse("This is the user page, <a href='/HalfFull/'>home</a>")

def make_a_crawl(request):
    return HttpResponse("This is the make a crawl page, <a href='/HalfFull/'>home</a>")

def pub_list(request):
    return HttpResponse("This is the pub list page, <a href='/HalfFull/'>home</a>")
