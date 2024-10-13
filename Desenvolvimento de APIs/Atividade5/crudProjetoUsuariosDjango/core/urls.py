from .views import ListCreateProjetoView, ListCreateUserView, RetrieveUpdateDestroyProjetoView, RetrieveUpdateDestroyUserView
from django.urls import path

urlpatterns = [
    path('projeto/', ListCreateProjetoView.as_view()),
    path('projeto/<int:pk>', RetrieveUpdateDestroyProjetoView.as_view()),
    path('usuario/',ListCreateUserView.as_view()),
    path('usuario/<int:pk>', RetrieveUpdateDestroyUserView.as_view())
]