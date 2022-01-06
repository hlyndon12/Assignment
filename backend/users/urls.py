from django.urls import path
from .views import *
urlpatterns = [  
    path("newsfeed/",newsfeed, name= 'newsfeed'),
    path("createpost/",createpost, name= 'createpost'),
]