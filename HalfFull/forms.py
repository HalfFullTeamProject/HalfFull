from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.models import User 
from HalfFull.models import UserProfile, Pub

class UserForm(forms.ModelForm): 
    
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password',)

    password = forms.CharField(widget=forms.PasswordInput())
class PubForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the pub name.")
    drinks = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 
    atmosphere = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    service = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False) 
    
    class Meta: 
        model = Pub 
        fields = ('name', 'picture',)
		
