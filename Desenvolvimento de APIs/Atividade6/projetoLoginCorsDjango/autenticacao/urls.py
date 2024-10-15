from .views import  ListCreateUserView, RetrieveUpdateDestroyUserView
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('',ListCreateUserView.as_view()),
    path('<int:pk>', RetrieveUpdateDestroyUserView.as_view()),
    path('signin', ObtainAuthToken.as_view())
]