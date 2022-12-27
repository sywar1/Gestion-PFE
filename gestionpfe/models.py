from django.db import models
from django.contrib.auth.models import User


class DemandeStageMonome(models.Model):
    userun=models.OneToOneField(User,on_delete=models.CASCADE)
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)  
    ncin=models.CharField(max_length=8) 
    parcours=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    
    
     
    def __str__ (self):
        return self.nom.capitalize()
    
    
    
class DemandeStageBinome(models.Model):
    binome1=models.OneToOneField(User,on_delete=models.CASCADE)
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)  
    ncin=models.CharField(max_length=8) 
    parcours=models.CharField(max_length=255) 
    email=models.EmailField(max_length=255)
    nom2=models.CharField(max_length=255)
    prenom2=models.CharField(max_length=255)  
    ncin2=models.CharField(max_length=8) 
    parcours2=models.CharField(max_length=255) 
    email2=models.EmailField(max_length=255) 
    
    def __str__ (self):
        return self.nom.capitalize()
    
class CahierCharge(models.Model):
    userr=models.OneToOneField(User,on_delete=models.CASCADE)
    nomprojet=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    besoinsf=models.CharField(max_length=25)
    delais=models.DateField()
    file1=models.FileField(upload_to= 'photos')
    file2=models.FileField(upload_to= 'photos')
    encadrant = models.ForeignKey("Encadrant", on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nomprojet.capitalize()
    
    
         
class Encadrant(models.Model):
    mail = models.EmailField(max_length=254)
    
    def __str__ (self):
        return self.mail.capitalize()
         
class FicheRecap(models.Model):
    etudiant=models.OneToOneField(User,on_delete=models.CASCADE)
    binom1=models.CharField(max_length=255)
    binom2=models.CharField(max_length=255)  
    typestage=models.CharField(max_length=255)
    Intitule=models.CharField(max_length=255)
    parcoursb1=models.CharField(max_length=255) 
    parcoursb2=models.CharField(max_length=255) 
    nomsociete=models.CharField(max_length=255)
    domainesociete=models.CharField(max_length=255) 
    datesoutenance=models.DateField()
    salle=models.CharField(max_length=255) 
    nomencadrant=models.CharField(max_length=255) 
    nomrapporteur=models.CharField(max_length=255) 
    nompresident=models.CharField(max_length=255) 
    
    def __str__ (self):
        return self.binom1.capitalize()
    
    
class Notifier(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    content = models.CharField(max_length=255,blank=True)
    
    

    
    

    
