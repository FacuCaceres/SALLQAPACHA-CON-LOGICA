from django.urls import path
from .import views
from django.conf.urls.static import static
app_name = 'app_acercade'

urlpatterns = [
    path('datosacercade/', views.acercaDe, name = 'boton_acercade')
    
]