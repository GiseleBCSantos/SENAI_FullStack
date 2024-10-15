from .views import ListCreateProjetoView,  RetrieveUpdateDestroyProjetoView
from django.urls import path

urlpatterns = [
    path('', ListCreateProjetoView.as_view()),
    path('<int:pk>', RetrieveUpdateDestroyProjetoView.as_view()),
    
]