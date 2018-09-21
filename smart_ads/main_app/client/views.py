# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from client.models import adsDetails, clientDetails
from client.forms import adsDetailsForm, clientDetailsForm
from django.contrib import messages

# Create your views here.

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
            form.save()
            print ('Ads updated successfully.')
            messages.success(request,'Ads updated successfully.')
    context = {'form': form}
    return render(request,'dashboard.html',context=context)

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