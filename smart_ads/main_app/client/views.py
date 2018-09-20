# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from client.models import adsDetails
from client.forms import adsDetailsForm

# Create your views here.

def clientads(request):
    my_record = adsDetails.objects.get(client_id_id=request.user.id)
    form = adsDetailsForm(instance=my_record)
    if request.POST:
        print ('inside')
        form= adsDetailsForm(request.POST, request.FILES,instance=my_record)
        save_it=form.save(commit = False)
        form.save()
        messages.success(request,'Business details updated successfully.')
    context = {'form': form}
    return render(request,'dashboard.html',context=context)