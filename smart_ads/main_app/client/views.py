# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from client.models import adsDetails, clientDetails
from client.forms import adsDetailsForm, clientDetailsForm
from django.contrib import messages

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from client.serializers import AdsSerializer
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def clientads(request):
    try:
        my_record = adsDetails.objects.get(client_id_id=request.user.id)
    except adsDetails.DoesNotExist:
        my_record = None


    form = adsDetailsForm(instance=my_record)
    if request.POST:
        print ('inside')
        form= adsDetailsForm(request.POST or None, instance=my_record)
        if form.is_valid():
            save_it = form.save(commit = False)
            print ('...')
            print (request.user.id)
            save_it.client_id_id = request.user.id
            save_it.update_flag=1
            form.save()
            print ('Ads updated successfully.')
            messages.success(request,'Ads updated successfully.')
    context = {'form': form}
    return render(request,'dashboard.html',context=context)

@login_required
def client_profile(request):
        try:
            my_record = clientDetails.objects.get(client_id_id=request.user.id)
        except clientDetails.DoesNotExist:
            my_record = None

        form = clientDetailsForm(instance=my_record)
        if request.POST:
            print ('inside')
            form = clientDetailsForm(request.POST or None, instance=my_record)
            if form.is_valid():
                save_it = form.save(commit=False)
                print ('...')
                print (request.user.id)
                save_it.client_id_id = request.user.id
                form.save()
                print ('Ads updated successfully.')
                messages.success(request, 'Ads updated successfully.')
        context = {'form': form}
        return render(request, 'profile.html', context=context)

@api_view(['GET','POST'])
def clientads_api(request):

    if request.method == 'GET':

        # contacts = adsDetails.objects.all()
        fallback_page_num = 'None'
        id = request.GET.get('id', fallback_page_num)
        ads = adsDetails.objects.filter(client_id_id=id)
        serializer = AdsSerializer(ads, many=True)

        print ("**** page ***: ", id)
        return Response(serializer.data)

    elif request.method == 'POST':
        print ("in post...")
        print (request.data[0])
        print (".......")
        data = request.data[0]
        # data['client_id']=  User.objects.get(id=request.data[0]['client_id'])
        # print (data)
        # test_data =  json.dumps(data)
        serializer = AdsSerializer(data=request.data[0])
        print (serializer)
        print (serializer.is_valid())
        if serializer.is_valid():
            print ('serializer is valid!')
            print (request.data[0]['client_id'])
            # serializer.client_id= User.objects.get(id=request.data[0]['client_id'])
            # serializer.save()
            my_record = adsDetails.objects.get(client_id_id=request.data[0]['client_id'])
            print ("/////")

            my_record.update_flag=0
            my_record.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)