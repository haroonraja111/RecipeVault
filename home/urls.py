from django.urls import path
from home.views import *

urlpatterns = [
    path('', home.index, name='home'),
      path('about/', about, name='about')
]
