from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, Prediction
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, neighbors, datasets
from django.http import HttpResponse, JsonResponse
import os
import json

@api_view(['POST'])
def prediction(request):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    df = pd.read_csv(os.path.join(__location__,'breast.csv'))
    df.replace('?', -99999, inplace=True)
    df.drop(['id'], 1, inplace=True)

    X = np.array(df.drop(['class'], 1))
    y = np.array(df['class'])

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)

    email = request.data['email']
    clump_thickness = int(request.data['clump_thickness'])
    unif_cell_size = int(request.data['unif_cell_size'])
    unif_cell_shape = int(request.data['unif_cell_shape'])
    marg_adhesion = int(request.data['marg_adhesion'])
    single_epith_cell_size = int(request.data['single_epith_cell_size'])
    bare_nuclei = int(request.data['bare_nuclei'])
    bland_chrom = int(request.data['bland_chrom'])
    norm_nucleoli = int(request.data['norm_nucleoli'])
    mistoses = int(request.data['mistoses'])

    prediction_xs = np.array([[clump_thickness,unif_cell_size,unif_cell_shape,marg_adhesion,single_epith_cell_size,bare_nuclei,bland_chrom,norm_nucleoli,mistoses]])
    prediction_xs = prediction_xs.reshape(len(prediction_xs), -1)

    prediction = clf.predict(prediction_xs)
    message = ""


    if int(prediction[0]) == 2:
        if accuracy >= 0.95:
            message = "Fortunately, You do not have cancer"
        else:
            message = "Fortunately, It's Benign !"
    else:
        message = "Unfortunately, It's Malignant !"


    owner = Account.objects.get(email=email)
    pred = Prediction(owner=owner, prediction=int(prediction[0]), accuracy = accuracy *100, comment="")
    pred.save()
    return Response({
        'accuracy' : accuracy * 100,
        'prediction' : prediction ,
        'message': message
    })

@api_view(['POST'])
def register(request):
    email = request.data['email']
    password = request.data['password']

    try:
        a = Account(email=email, password=password, type="patient")
        a.save()
    except:
        return Response({"already registered"})
    return Response({"register"})

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
def dlogin(request):
    email = request.data['email']
    password = request.data['password']

    try:
        a = Account.objects.get(email=email)
        if a.password == password:
            if a.type == "doctor":
                return Response("login")
            else:
                return Response("not a doctor")
        else:
            return Response("invalid credentials")
    except:
        return Response({"You need to register"})

@api_view(['POST'])
def get_predictions_per_user(request):
    email = request.data['email']

    try:
        owner = Account.objects.get(email=email)
        result = list(Prediction.objects.filter(owner = owner).values())
        print(result)
    except:
        result = []
    return JsonResponse({'data':result})

@api_view(['POST'])
def get_predictions_for_doctor(request):
    try:
        result = list(Prediction.objects.all().values())
    except:
        result = []
    return Response({'data':result})

@api_view(['Post'])
def create_comment(request):
    id = request.data['id']
    comment = request.data['comment']

    pred = Prediction.objects.get(id=id)
    pred.comment = comment
    pred.save()

    return Response("done")