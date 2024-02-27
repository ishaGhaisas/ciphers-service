from django.urls import path
from .views import encode, greetings

urlpatterns = [
    path('', greetings),
    path('caesar/<str:plain_text>/<int:shift>', encode),
]