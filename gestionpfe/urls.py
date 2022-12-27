from django.urls import path
from . import views
from django.views.static import serve 

app_name="gestionpfe"
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.register_request,name='signup'),
    path('monome/',views.monome,name='monome'),
    path('binome/',views.binome,name='binome'),
    path('updatebinome/',views.updateDatabinome,name="updatebinome"),
    path('updatemonome/',views.updateDatamonome,name="updatemonome"),
    path('CahierCharge/',views.cahierC,name='demandeC'),
    path('ficherecap/',views.ficherecap,name='ficherecap'),
    path('test/',views.subscribe,name='subscribe'),
    path("reponse/<int:pk>/<slug:userlogin>/",views.reponse,name='reponse'),
    path("notif/",views.notifier,name='notifier'),
    
    
    
    
]

