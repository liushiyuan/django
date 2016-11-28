from django.shortcuts import render
from eqshow.models import EqshowPost
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def doPost(request):
    value = ""
    if request.method == "POST":
        for key in request.POST:
            value += request.POST[key]
            value += ","
        value = value.split(',')
        eqshowpost = EqshowPost()
        eqshowpost.phone = value[0]
        eqshowpost.enterprise = value[1]
        eqshowpost.name = value[2]
        eqshowpost.save()
    return HttpResponse("ok")
