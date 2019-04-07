from .serializers import BhojanalayaDetailsSerializers, BhojanalayaAddressSerializers
from rest_framework import generics
from bhojanalayas.models import Address, Details
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json


class BhojanalayaDetailsView(generics.ListCreateAPIView):

    queryset = Details.objects.all()
    serializer_class = BhojanalayaDetailsSerializers


class BhojanalayaAddressView(generics.ListCreateAPIView):

    queryset = Address.objects.all()

    serializer_class = BhojanalayaAddressSerializers


@api_view(['GET', 'POST'])
def mapLocation(request):
    global reqName
    responseData = []
    responses = {}
    if (request.method == 'POST'):
        try:
            reqName = str(request.body)
            reqName = reqName[2:len(reqName) - 1]
            print(reqName)

            return Response(status.HTTP_200_OK)

        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

    if (request.method == 'GET'):
        try:
            print("GOT into get section")
            all_details = list(
                Address.objects.filter(rest_id_id=reqName).values_list(
                    'latitude', 'longitude'))

            print(all_details)
            for e in all_details:
                responses = {}
                responses['latitude'] = e[0]
                responses['longitude'] = e[1]

                # responseData.append(responses)
            print(responses)
            return Response(responses, status.HTTP_200_OK)
            # return Response(status.HTTP_200_OK)

        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def registerUser(request):
    global reqUserCred
    global created
    if (request.method == 'POST'):

        try:
            reqUserCred = str(request.body)

            reqUserCred = json.loads(reqUserCred[2:len(reqUserCred) - 1])
            print(reqUserCred["username"])
            u, created = User.objects.get_or_create(
                username=reqUserCred["username"])

            print(u, created)
            success = "Registeration not Done"
            if created:
                u.set_password(reqUserCred["password"])
                success = "User got registered! Proceed with login"
                u.save()

            else:
                print(u.password)
                # success = "Done"
                success = "User got registered! Proceed with login"
                # answer = authenticate(username='hello', password='world')
                # print(answer)

            return Response(success, status.HTTP_200_OK)

        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

    # elif (request.method == 'GET'):
    #     try:

    #         success = created
    #         print(success)
    #         return Response(success, status.HTTP_200_OK)

    #     except ValueError as e:
    #         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def loginUser(request):
    global reqUserCred

    if (request.method == 'POST'):

        try:
            reqUserCred = str(request.body)

            reqUserCred = json.loads(reqUserCred[2:len(reqUserCred) - 1])
            print(reqUserCred["username"])

            loginCheck = authenticate(
                username=reqUserCred["username"],
                password=reqUserCred["password"])
            print(loginCheck)
            if loginCheck is not None:
                result = "Login successful"
            else:
                result = "Login failed"
            return Response(result, status.HTTP_200_OK)

        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

    # elif (request.method == 'GET'):
    #     try:

    #         success = created
    #         print(success)
    #         return Response(success, status.HTTP_200_OK)

    #     except ValueError as e:
    #         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
