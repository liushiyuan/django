from django.shortcuts import render, render_to_response
from models import Pic
from django.template import RequestContext

# Create your views here.

def home(request):
    pics = Pic.objects.all()
    if request.method == "POST":
            headImg = request.FILES.getlist('headImg')
            for picture in headImg:
                pic = Pic()
                pic.headImg = picture
                pic.save()
    return render_to_response('home.html', {'pics':pics}, context_instance = RequestContext(request))
