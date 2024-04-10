from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer

'''
IMPORTANT: Ask GPT what the body does.
'''
@api_view(['GET'])
def getRoutes (request):

    routes = [
        {
            'Endpoint': '/api/',
            'method': 'GET',
            'body': 'None',
            'description': 'Returns an array of endpoints.'
        },
        {
            'Endpoint': '/api/post',
            'method': 'POST',
            'body': {"body":""},
            'description': 'Retrieves data from front-end container.'
        },
        {
            'Endpoint': '/api/recent',
            'method': 'GET',
            'body': {"body":""},
            'description': 'Returns recent web address queries'
        }
    ]

    return Response(routes)

'''
Gets the recent web address queries
'''
@api_view(['GET'])
def getRecentQueries (request):
    queries = Address.objects.all()
    serializer = AddressSerializer(queries, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    if request.method == 'POST':

        data = request.data # Extract
        serializer = AddressSerializer(data=data) # Serialize into an object
        
        # Validate
        if serializer.is_valid():
            serializer.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        