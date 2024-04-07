from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
        },
        {
            'Endpoint': 'api/get',
            'method': 'GET',
            'body': None,
            'description': "Returns output from scraping and AI generation."
        }
    ]

    return Response(routes)

'''
Gets the latest request for a web page.
'''
@api_view(['GET'])
def getResponse (request):
    return Response('Notes')

'''
Gets the recent web address queries
'''
@api_view(['GET'])
def getRecentQueries (request):
    queries = Address.objects.all()
    serializer = AddressSerializer(queries, many=True)
    return Response(serializer.data)