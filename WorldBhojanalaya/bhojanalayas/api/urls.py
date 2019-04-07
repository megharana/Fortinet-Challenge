from django.contrib import admin
from django.urls import path
from .views import BhojanalayaDetailsView, BhojanalayaAddressView, mapLocation, registerUser, loginUser

app_name = 'bhojanalayas'
urlpatterns = [
    path(
        'details/', BhojanalayaDetailsView.as_view(),
        name='resturant-details'),
    path(
        'address/', BhojanalayaAddressView.as_view(),
        name='resturant-details'),
    path('getId/', mapLocation, name='resturant-details'),
    path('getSignUpCred/', registerUser, name='resturant-details'),
    path('getLoginInfo/', loginUser, name='resturant-details')
]
