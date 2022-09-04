from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account

@api_view(['POST'])
def prediction(request):
    # print(request.data['email'])
    return Response({"Hello World! "})

@api_view(['POST'])
def register(request):
    email = request.data['email']
    password = request.data['password']

    try:
        a = Account(email=email, password=password, type="patient")
        a.save()
    except:
        return Response({"already registered"})
    return Response({"Register"})

@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    try:
        a = Account.objects.get(email=email)
        if a.password == password:
            return Response("login")
        else:
            return Response("invalid credentials")
    except:
        return Response({"You need to register"})

@api_view(['POST'])
def get_predictions_per_user(request):
    return Response({"get_predictions_per_user"})

@api_view(['POST'])
def get_predictions_for_doctor(request):
    return Response({"get_predictions_for_doctor"})