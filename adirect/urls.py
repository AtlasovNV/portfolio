from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import adirect.views as adirect

app_name = 'adirect'

urlpatterns = [
    path('', adirect.adirect, name='adirect'),
    path('team/', adirect.team, name='team'),
    path('Generator/', adirect.Generator, name='Generator'),
    path('ServiceGenerator/', adirect.ServiceGenerator, name='ServiceGenerator'),
]