from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def login(request):
    body = json.loads(request.body)
    user = authenticate(username=body["username"], password=body["password"])
    response = {}
    if user is not None:
        response["success"] = "You have succesfully logged in"
        return HttpResponse(json.dumps(response), status=200, content_type='application/json')
    else:
        response["error"] = "Login detials are incorrect"
        return HttpResponse(json.dumps(response), status=401, content_type='application/json')
