from os import name
from django.urls.conf import path
from backend import views

urlpatterns = [
    path('about/',views.About,name='About'),
    path('',views.Home,name = 'home'),
    path('Partners/',views.Partners,name='Partners'),
    path('news/',views.News,name='news'),
    path('Charities/',views.Charities,name='Charities'),
    path('Elderly/',views.Elderly,name = 'Elderly'),
    path('Archive/',views.Archive,name="Archive"),
    path('videogallery/',views.VideoGalary,name='VideoGallary'),
    path('Photogallery/',views.PhotoGalary,name='photos'),
 
    
   
    
        
    
    
]