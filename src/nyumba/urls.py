from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'nyumba'

urlpatterns = [
    #landlord urls
    path('landlord_home/', views.landlord_home, name='landlord_home'),
    path('properties/', views.properties, name='properties'),
    path('individual_property/', views.individual_property, name='individual_property'),
    #tenant urls
    path('tenant_home/', views.tenant_home, name='tenant_home'),
    #common urls
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)