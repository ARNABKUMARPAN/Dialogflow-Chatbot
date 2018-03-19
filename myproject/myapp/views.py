from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.conf import settings
#import dialogflow
import apiai
import json

def bb(request):
    return HttpResponse("hchena")
def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data


@require_http_methods(['GET'])
def index_view(request):
    return render(request, 'app.html')


@require_http_methods(['POST'])
def chat_view(request):
    #dialogflow_ = dialogflow(**settings.DIALOGFLOW)
    input_dict = convert(request.body)
    input_text = json.loads(input_dict)['text']
    print ("input text",input_text)
    #responses = dialogflow_.text_request(str(input_text))
    access_token = 'cab0e92861494ed2bddff46324771fe4'
    client = apiai.ApiAI(access_token)
    request_1 = client.text_request()
    request_1.query =input_text
    #print(request.query)
    #request_1.query = "Today is 13th December, 2018" # or whatever other input the user puts
    byte_response = request_1.getresponse().read()
    json_response = byte_response.decode('utf8')#.replace("'", '"') # replaces all quotes with double quotes
    json_obj = json.loads(json_response)
    print (json_obj['result']['fulfillment']['speech'])
    if request.method == "GET":
        # Return a method not allowed response
        data = {
            'detail': 'You should make a POST request to this endpoint.',
            'name': '/chat'
        }
        return JsonResponse(data, status=405)
    elif request.method == "POST":
        data = {
            'text': str(json_obj['result']['fulfillment']['speech']),
        }
        return JsonResponse(data, status=200)
        #return HttpResponse(json_obj['result']['fulfillment'])
    elif request.method == "PATCH":
        data = {
            'detail': 'You should make a POST request to this endpoint.',
            'name': '/chat'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)

    elif request.method == "DELETE":
        data = {
            'detail': 'You should make a POST request to this endpoint.',
            'name': '/chat'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)
