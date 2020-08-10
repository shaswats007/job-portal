from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', FileUploadView.as_view()),
    path('',include('student.urls'))
]