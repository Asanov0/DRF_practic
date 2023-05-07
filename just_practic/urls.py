from django.urls import path, include
from just_practic.views import *



app_name = 'just_practic'
urlpatterns = [
    # path('', test, name='test'),
    path('', CarCreateView.as_view()),
]
