from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import adirect.views as adirect

app_name = 'adirect'

urlpatterns = [
    path('', adirect.adirect, name='adirect'),
    path('team/', adirect.team, name='team'),
    path('keyword/generator/', adirect.Generator, name='Generator'),

    path('ServiceGenerator/', adirect.ServiceGenerator, name='ServiceGenerator'),

    path('keyword/inclinator', adirect.inclinator, name='inclinator'),
    path('keyword/wordcount', adirect.wordcount, name='wordcount'),
    path('keyword/crossminus', adirect.CrossMinus, name='crossminus'),
    path('keyword/lemmatizer', adirect.lemmatizer, name='lemmatizer'),
    path('keyword/synonymizer', adirect.synonymizer, name='synonymizer'),
    path('keyword/trimutm', adirect.TrimUtm, name='trimutm'),
    path('keyword/cityremover', adirect.CityRemover, name='cityremover'),

]