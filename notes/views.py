from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Note
from django.utils import timezone


@csrf_exempt
def index(request):
    if request.method == 'GET':
        all_notes = list(Note.objects.values())
        return JsonResponse({"notes": all_notes})

    if request.method == 'POST':
        # if request.user.is_authenticated:
        #     print(request.user)
        body = json.loads(request.body)
        user = User.objects.get(username=body['username'])
        note = Note(note_text=body["text"],
                    pub_date=timezone.now(), owner=user)
        note.save()
        response = {}
        response["success"] = "Note successfully added"
        return HttpResponse(json.dumps(response), status=200, content_type='application/json')
