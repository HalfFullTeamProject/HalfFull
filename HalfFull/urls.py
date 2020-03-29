from django.urls import path
from HalfFull import views

app_name = 'HalfFull'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name ='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('userpage/', views.userpage, name='userpage'),
    path('make_a_crawl/', views.make_a_crawl, name='make_a_crawl'),
    path('pub_list/', views.pub_list, name='pub_list'),
    path('add_a_pub/', views.add_a_pub, name='add_a_pub'),
]