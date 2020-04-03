from django.shortcuts import render
from django.http import HttpResponse
from HalfFull.forms import UserForm, PubForm#, #CrawlForm
from HalfFull.models import Pub, UserProfile

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('HalfFull:home'))
            else:
                return HttpResponse("Your HalfFull account is disabled.")
                
        else:
            print(f"Invalid login details: {username}, {password}") 
            return HttpResponse("Invalid login details supplied.")
            
    else:
        return render(request, 'HalfFull/login.html')

def signup(request):
    registered=False
    
    if request.method == 'POST':
    
        user_form = UserForm(request.POST)

    
        if user_form.is_valid(): 
            user = user_form.save() 
            user.set_password(user.password)
            user.save()
        
            registered=True
        else:
            print(user_form.errors)
            
    else:
        user_form = UserForm()
        
    return render(request, 'HalfFull/signup.html', context = {'user_form': user_form, 'registered': registered})

def userpage(request):
    context_dict = {}
    return render(request, 'HalfFull/userpage.html', context=context_dict)

def make_a_crawl(request):
    context_dict = {}
    
    userprofile = UserProfile(user=request.user)
    userprofile.save()
    crawls = userprofile.crawl.all()
    context_dict['crawls'] = crawls
    
    return render(request, 'HalfFull/make_a_crawl.html', context=context_dict)

def pub_list(request):
    context_dict = {}
	
    pubs = Pub.objects.all()
    context_dict['pubs'] = pubs
    
    user1 = request.user
    
    if request.method == 'POST':
        name = pub.name
        atmosphere=pub.atmosphere
        service=pub.service
        drinks=pub.drinks
        picture=pub.picure
        crawl1 = pub(name = pub.name, atmosphere=pub.atmosphere, service=pub.service, drinks=pub.drinks, picture=pub.picure)
        crawl1.save()
        user1.crawl.add(crawl1)
	
    return render(request, 'HalfFull/pub_list.html', context=context_dict)
    
def add_a_pub(request):
    form = PubForm
    
    if request.method == 'POST':
        form = PubForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('/HalfFull/home/')
        else:
            print(form.errors)
            
    return render(request, 'HalfFull/add_a_pub.html', {'form':form})    
    

