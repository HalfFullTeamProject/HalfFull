from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.models import User 
from HalfFull.models import UserProfile, Pub

class UserForm(forms.ModelForm): 
    
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password',)

    password = forms.CharField(widget=forms.PasswordInput())
    
#class CrawlForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile
#        fields = ('crawl',)
        
class PubForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the pub name.")
    drinks = forms.IntegerField(min_value = 0, max_value=5, help_text="how would you rate this pubs drinks") 
    atmosphere = forms.IntegerField(min_value = 0, max_value=5, help_text="how would you rate this pubs atmosphere")
    service = forms.IntegerField(min_value = 0, max_value=5, help_text="how would you rate the service of this pub")
    
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False) 
    
    class Meta: 
        model = Pub 
        fields = ('name', 'picture',)
        

        


