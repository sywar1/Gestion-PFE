from multiprocessing import context
from urllib import request
from django.shortcuts import  render, redirect
from .forms import NewUserForm, SubscribeForm
from django.contrib.auth import login
from .models import *
from .models import DemandeStageBinome
from .models import CahierCharge
from .models import FicheRecap
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import get_template 
from django.core.mail import EmailMessage
from django.template import loader



# Create your views here.
def home(request):
    return render(request,'index.html')

    
def register_request(request):
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("gestionpfe:home")
    form=NewUserForm()
    return render(request,"register/signup.html",context={"register_form":form})
        
        
def monome(request):
    user=0
    re='parts/monome.html'
    if request.method == "POST":
        cin1=request.POST.get('cin')
        email1=request.POST.get('email')
        parcour1=request.POST.get('parcours')
        nom1=request.POST.get('nom')
        prenom1=request.POST.get('prenom')
        DemandeStageMonome.objects.create(userun=request.user,nom=nom1,prenom=prenom1,ncin=cin1,parcours=parcour1,email=email1)
        return render(request,'parts/document.html',{"cin":cin1,"nom":nom1,"prenom1":prenom1,"parcour":parcour1,"email":email1})
    try:
        user=DemandeStageMonome.objects.get(userun=request.user)
        re='parts/updatemonome.html'
    except:
        pass
    return render(request,re,{'user':user})

def updateDatamonome(request):
    if request.method == "POST":
        user=DemandeStageMonome.objects.get(userun=request.user)
        user.nom=request.POST.get('nom')
        user.prenom=request.POST.get('prenom')
        user.ncin=request.POST.get('cin')
        user.parcours=request.POST.get('parcours')
        user.email=request.POST.get('email')
        user.save()
        return render(request,'parts/document4.html',{'user':user})
    return render(request,'parts/updatemonome.html',{'user':user})

def binome(request):
    user=0
    temp='parts/binome.html'
    if request.method == "POST":
        ncin1=request.POST.get('cin1')
        mail=request.POST.get('mail1')
        parcour=request.POST.get('parcours1')
        nome=request.POST.get('nom1')
        prenome=request.POST.get('prenom1')
        ncinn=request.POST.get('cin2')
        maill=request.POST.get('mail2')
        parcourr=request.POST.get('parcours2')
        nomm=request.POST.get('nom2')
        prenomm=request.POST.get('prenom2')
        DemandeStageBinome.objects.create(binome1=request.user,nom=nome,prenom=prenome,ncin=ncin1,parcours=parcour,email=mail,nom2=nomm,prenom2=prenomm,ncin2=ncinn,parcours2=parcourr,email2=maill)
        return render(request,'parts/document2.html',{"cin1":ncin1,"nom1":nome,"prenom1":prenome,"parcours1":parcour,"email1":mail,"cin2":ncinn,"nom2":nomm,"prenom2":prenomm,"parcours2":parcourr,"email2":maill})
    try:
        user=DemandeStageBinome.objects.get(binome1=request.user)
        temp='parts/update.html'
    except :
        pass
    return render(request,temp,{'user':user})  


def updateDatabinome(request):
    if request.method == "POST":
        user=DemandeStageBinome.objects.get(binome1=request.user)
        user.nom=request.POST.get('nom1')
        user.prenom=request.POST.get('prenom1')
        user.ncin=request.POST.get('cin1')
        user.parcours=request.POST.get('parcours1')
        user.email=request.POST.get('mail1')
        user.nom2=request.POST.get('nom2')
        user.prenom2=request.POST.get('prenom2')
        user.ncin2=request.POST.get('cin2')
        user.parcours2=request.POST.get('parcours2')
        user.email2=request.POST.get('mail2')
        user.save()
        return render(request,'parts/document3.html',{'user':user})



def cahierC(request):
    enc=Encadrant.objects.all()
    if request.method == "POST":
        nomp=request.POST.get("projet")
        desc=request.POST.get("descrip")
        besoins=request.POST.get("besoin")
        dell=request.POST.get("delai")
        fil1=request.FILES.get("document")
        fil2=request.FILES.get("document2")
        mailo = request.POST.get("email")
        enc=Encadrant.objects.get(id=mailo)
        subscribe(request.user,besoins,desc,nomp,dell,enc.mail)
        CahierCharge.objects.create(userr=request.user,nomprojet=nomp,description=desc,besoinsf=besoins,delais=dell,file1=fil1,file2=fil2,encadrant=enc)
        messages.success(request, 'votre cahier de charge est bien envoye !')
        return render(request,'parts/CahierCharge.html',{"projet":nomp,"descrip":desc,"besoin":besoins,"delai":dell,"file1":fil1,"file2":fil2,'email': mailo})
    return render(request,'parts/CahierCharge.html',{'notes': enc})


def ficherecap(request):
    if request.method == "POST":
        b1=request.POST.get('nom1')
        b2=request.POST.get('nom2')
        types=request.POST.get('type')
        intitul=request.POST.get('intitul')
        parcour=request.POST.get('parcours1')
        parcour2=request.POST.get('parcours2')
        noms=request.POST.get('nomso')
        domaine=request.POST.get('domaine')
        dat=request.POST.get('date')
        salle=request.POST.get('sale')
        nomen=request.POST.get('nome')
        nompr=request.POST.get('nomp')
        nomr=request.POST.get('nomr')
        FicheRecap.objects.create(etudiant=request.user,binom1=b1,binom2=b2,typestage=types,Intitule=intitul,parcoursb1=parcour,parcoursb2=parcour2,nomsociete=noms,domainesociete=domaine,datesoutenance=dat,salle=salle,nomencadrant=nomen,nomrapporteur=nompr,nompresident=nomr)
        messages.success(request, 'Success!')
        return render(request,'parts/ficherecap.html',{"bi1":b1,"bi2":b2,"typ":types,"Intitule":intitul,"parcoursb1":parcour,"parcoursb2":parcour2,"nomsociete":noms,"domainesociete":domaine,"datesoutenance":dat,"salle":salle,"nomencadrant":nomen,"nomrapporteur":nompr,"nompresident":nomr})
        
    return render(request,'parts/ficherecap.html')
    
  

    
def subscribe(userr,besoinsf,description,nomprojet,delais,mail):
    #Cahier=CahierCharge.objects.get(userr=request.user)
    template= loader.get_template('welcome.html').render({'name':userr,'nomprojet':nomprojet,'description':description,'besoin':besoinsf,'delais':delais})
    email=EmailMessage(
        'this is my cahier de charge',
        template,
        settings.EMAIL_HOST_USER,
        [mail]
    )
    # render template to html
    email.content_subtype = 'html'
    email.fail_silently=False
    email.send()
    
    

def reponse(request,pk,userlogin):
    userl=User.objects.get(username=userlogin)
    Notifier.objects.create(user=userl,content=pk)
    return render(request,'parts/response.html')

def notifier(request):
    noti=Notifier.objects.filter(user=request.user)
    return render(request,'notif.html',{'noti':noti})
    


        
     


    


    

    

        
    


 

        
	    
     
    
        
	   
	
   


    
    
    
        
    