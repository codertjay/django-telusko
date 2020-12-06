from django.urls import path

from calc import views


urlpattern = [
    path('',views.home , name='home')
]
