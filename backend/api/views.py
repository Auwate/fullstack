from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer, OpenAISerializer
from openai import OpenAI

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
            'Endpoint': '/api/post/',
            'method': 'POST',
            'body': {"body":""},
            'description': 'Retrieves data from front-end container.'
        },
        {
            'Endpoint': '/api/recent/',
            'method': 'GET',
            'body': {"body":""},
            'description': 'Returns recent web address queries'
        },
        {
            'Endpoint': '/api/response/',
            'method': 'GET',
            'body': {"body":""},
            'description': 'Returns the ChatGPT response'
        }
    ]

    return Response(routes)


'''
Gets the ChatGPT response
'''
@api_view(['GET'])
def getResponse (request):
    
    addr = Address.objects.last()

    if addr: # Check if the database returned an object

        api_key = None
        with open('api_key', 'r') as file:
            api_key = file.read().strip()

        if not api_key:
            return Response({"message": "API key not found! You may have forgot to add it in the api_key.txt file."}, status=status.HTTP_400_BAD_REQUEST)
        
        client = OpenAI(api_key=api_key) # ChatGPT API

        response = client.chat.completions.create ( # Send API request
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Explain to me who" + addr.body + "is and what" + addr.body + "might contain. Do not tell me that you cannot browse, I already know."}],
        )
        # Serialize for sending through HTTP
        serializer = OpenAISerializer(data={'response': response.choices[0].text})
        # Check if serializer was correct
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Database Error: No recent queries"}, status=status.HTTP_400_BAD_REQUEST)

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
