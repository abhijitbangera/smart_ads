"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app import views as main_app_view
from client.views import clientads, client_profile, clientads_api
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',main_app_view.test, name='test' ),
    url('dashboard/$', main_app_view.dashboard, name='dashboard'),
    url('dashboard/myads$', clientads, name='clientads'),
    url('dashboard/profile$', client_profile, name='client_profile'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name="client_login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="index.html"), name="logout"),
    url(r'^api/clientads/$',clientads_api, name='clientads_api'), # http://127.0.0.1:8000/api/clientads/?id=1
    url(r'^api/post_clientads/$',clientads_api, name='clientads_api'), # http://127.0.0.1:8000/api/post_clientads/

]
