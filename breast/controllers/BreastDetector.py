import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, neighbors, datasets
from django.http import HttpResponse, JsonResponse
import os

def predict(req):
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


    clump_thickness = int(req.GET['clump_thickness'])
    unif_cell_size = int(req.GET['unif_cell_size'])
    unif_cell_shape = int(req.GET['unif_cell_shape'])
    marg_adhesion = int(req.GET['marg_adhesion'])
    single_epith_cell_size = int(req.GET['single_epith_cell_size'])
    bare_nuclei = int(req.GET['bare_nuclei'])
    bland_chrom = int(req.GET['bland_chrom'])
    norm_nucleoli = int(req.GET['norm_nucleoli'])
    mistoses = int(req.GET['mistoses'])

    prediction_xs = np.array([[clump_thickness,unif_cell_size,unif_cell_shape,marg_adhesion,single_epith_cell_size,bare_nuclei,bland_chrom,norm_nucleoli,mistoses]])
    prediction_xs = prediction_xs.reshape(len(prediction_xs), -1)

    prediction = clf.predict(prediction_xs)
    print(prediction)
    return JsonResponse({
        'accuracy' : accuracy,
        'prediction' : int(prediction[0])
    })
