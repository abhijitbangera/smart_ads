from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def test(request):
    return render(request, 'index.html', context={})


def client_login(request):
    return render(request, 'client_login.html', context={})

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html', context={})
