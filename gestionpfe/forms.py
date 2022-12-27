from xml.etree.ElementTree import tostring
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from gestionpfe.models import DemandeStageBinome, DemandeStageMonome

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
class SubscribeForm(forms.Form):
    email = forms.EmailField()
        

 
 


	

    

       

	
        
            
        