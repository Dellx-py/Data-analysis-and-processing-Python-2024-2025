from django.urls import path
from .views import random_view, alege_view
# URL MIC DIN PAROLA
urlpatterns = [
   path('random', random_view),
   path('alege', alege_view),
]
