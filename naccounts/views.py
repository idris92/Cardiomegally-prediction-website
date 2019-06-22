from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.contrib.auth.models import User
from django.contrib import messages,auth
from sklearn.externals import joblib
import os
from django.http import JsonResponse
from .models import Prediction




def dashboard(request):
        
        if request.method=='POST':
                
                report = request.POST['report']
                patient_id = request.POST['patient_id']
                model=joblib.load('naccounts/piped.pkl')
                predictions=model.predict([report])
                #print (prediction)
                messages.success(request, (predictions[0]))
                prediction=Prediction(patient_id=patient_id,report=report,predictions=predictions[0])
                prediction.save()
                return render(request, 'naccounts/dashboard.html')

                
        else:

                return render(request,'naccounts/dashboard.html')
        



def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('index')
        
    else:
        return render(request,'index')







def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


