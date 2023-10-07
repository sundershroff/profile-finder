from django.shortcuts import render , redirect
from django.http import HttpResponse
# from .forms import *
from .models import *
from chat.models import Thread
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
import cv2
from django.http import JsonResponse
import requests
from django.urls import reverse

import random
import string

import PyPDF2
import re
import datetime

import base64
from io import BytesIO
from PIL import Image

from django.db import connections
# Create your views here.
from django.core import serializers
from django.http import HttpResponse

all_url = "http://127.0.0.1:3000/"
def signin(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post(all_url+"pi_signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/pi_admin_dashboard/{uidd}")
        else:
            error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
        
    context = {'error':error}
    return render(request,"pi_signin.html",context)


def signup(request):
    error = ""
    if request.method == "POST":
        
        if request.POST['password'] == request.POST['confirm_password']:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post(all_url+'pi_signup/',data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 302:
                   error = "User Already Exist"
                else:
                   return redirect(f"/pi_otpcheck/{uidd}")      
    context = {'error':error}
        
    return render(request,'pi_signup.html',context)

def opt_check(request,id):
    # form1 = ProfileOtpForm()
    # get = requests.get(f" http://127.0.0.1:3000/otp/{id}").json()
    # print(get['otp'])
    # print(get['uid'])
    context = {'invalid':"invalid"}
    new=[]
    if request.method == "POST":
        new.append(request.POST["otp1"])
        new.append(request.POST["otp2"])
        new.append(request.POST["otp3"])
        new.append(request.POST["otp4"])
        data = {
            'user_otp':int(''.join(new).strip())
           
        }
        print(data)
        # response = requests.post(f"http://54.159.186.219:8000/otp/{id}",   data=data)
        response = requests.post(f"http://127.0.0.1:3000/pi_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/pi_profilepicture/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}

    return render(request,'pi_otpcheck.html',context)

def profile_picture(request,id):
    if request.method == "POST":
        print(request.POST)
        # response = requests.post(f"http://54.159.186.219:8000/profilepicture/{id}",files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/pi_profilePicture/{id}",files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/pi_complete_profile/{uidd}")
        # else:
            # return HttpResponse("INVALID data")
    return render(request,"pi_profilepicture.html")

def complete_profile(request,id):
    if request.method == "POST":
        print(request.POST)
        # response = requests.post(f"http://54.159.186.219:8000/profilepicture/{id}",files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/pi_complete_account/{id}",data = request.POST,files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/pi_admin_dashboard/{uidd}")
        # else:
            # return HttpResponse("INVALID data")
    return render(request,"uploadprofile.html")

def admin_dashboard(request,id):
        return render(request,"admin_dashboard.html")

def profile(request,id):
        return render(request,"profile.html")

def edit_profile(request,id):
        return render(request,"edit_profile.html")

def payment(request,id):
        return render(request,"pi_payment1.html")

def client_list(request,id):
        return render(request,"client_list.html")

def client_details(request,id):
        return render(request,"client_details.html")


def subscription(request,id):
        return render(request,"pi_subscription.html")

def payment_table(request,id):
        return render(request,"pi_payment_table.html")


def add_client(request,id):
        return render(request,"pi_add_new_client.html")


def client_feedback(request,id):
        return render(request,"pi_client_feedback.html")

def setting(request,id):
        return render(request,"pi_Account_Settings.html")

