from django.urls import path
from .launchapp import views

urlpatterns = [
    path('launch/', views.get_data)
]
