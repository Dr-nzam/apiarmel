from django.urls import path
from .views import toto

urlpatterns = [
    path('', toto, name='toto' )
]
