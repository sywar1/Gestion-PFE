import statistics
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gestionpfe.urls',namespace='gestionpfe')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('social-auth/', include('social_django.urls', namespace="social")),
    
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)