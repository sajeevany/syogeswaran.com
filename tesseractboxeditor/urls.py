from django.conf.urls import url, include
from django.contrib import admin

app_name = 'tesseractboxeditor'
urlpatterns = [
    url(r'^', 'tesseractboxeditor.views.tbe', name='tbe'),
]