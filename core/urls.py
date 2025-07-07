from django.urls import path,include
from core.views import home,contact,tracking,menu,reservation
urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('tracking/',tracking,name='tracking'),
    path('menu/',menu,name='menu'),
    path('reservation/',reservation,name='reservation'),
]