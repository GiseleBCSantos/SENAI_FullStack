from django.urls import path
from .views import ListCreateProjetoAPIView, RetrieveUpdateDestroyProjetoAPIView

urlpatterns = [
    path('', ListCreateProjetoAPIView.as_view()),
    path('<int:pk>', RetrieveUpdateDestroyProjetoAPIView.as_view())
]