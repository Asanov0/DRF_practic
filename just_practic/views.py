from django.shortcuts import render, HttpResponse
from rest_framework import generics
from just_practic.serializers import CarDetailSerializer


def test(request):
    return HttpResponse('hello every one is this work ?')



class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
   