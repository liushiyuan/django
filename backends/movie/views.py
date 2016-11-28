from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import urllib
import json
# Create your views here.

def doGetList(webURL, page):
    content = ""
    lastpage = ""
    try:
        response = urllib.urlopen(webURL)
        result = response.read()
	content = result.split("<ul class=\"movie-list reset\">")[1]
        content = content.split("</ul>")[0]
        if content.count("<") == 0:
            content = result.split("<ul class=\"tv-list list none\">")[1]
            content = content.split("</ul>")[0]
        if page == "1":
            try:
                lastpage = result.split("<a class=\"last\"")[1]
                lastpage = lastpage.split(">")[0]
                lastpage = lastpage.split("/")[-1]
                lastpage = lastpage.split("\"")[0]
            except Exception, e:
                lastpage = "1"
        data = {"content":content, "lastpage":lastpage}
        data = json.dumps(data)
    except Exception, e:
        data = "failed"
    return data

@csrf_exempt
def getList(request, page):
    webURL = "http://www.rs05.com/%s" % (page)
    data = doGetList(webURL, page)
    return HttpResponse(data)

@csrf_exempt
def getTvDes(request, name):
    webURL = "http://%s" % (name)
    title = ""
    try:
        response = urllib.urlopen(webURL)
        result = response.read()
        content = result.split("<div class=\"body\">")[1]
        content = content.split("</h1>")[1]
        content = content.split("<script")[0]
        content = "<div>%s" % content
    except Exception, e:
        content = "failed"
    model_content = "<div class=\"modal-header\"> \
                         <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">&times;</button> \
                         <h4 class=\"modal-title\" id=\"myModalLabel\"> \
                         %s \
                         </h4> \
                     </div> \
                    <div class=\"modal-body\"> \
                    %s \
                    </div> \
                    <div class=\"modal-footer\"> \
                        <button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\"> \
                        Close \
                        </button> \
                    </div>" % (title, content)
    return HttpResponse(model_content)

@csrf_exempt
def getMovieDes(request, name):
    webURL = "http://www.rs05.com/%s" % (name)
    try:
        response = urllib.urlopen(webURL)
        result = response.read()
        content = result.split("<h1>")[1]
        content = content.split("</h1>")
        title = content[0]
        content = content[1]
        content = content.split("</div>")
        content = "%s</div>%s</div>%s</div>" % (content[1], content[2], content[3])
    except Exception, e:
        content = "failed"
    model_content = "<div class=\"modal-header\"> \
                         <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">&times;</button> \
                         <h4 class=\"modal-title\" id=\"myModalLabel\"> \
                         %s \
                         </h4> \
                     </div> \
                    <div class=\"modal-body\"> \
                    %s \
                    </div> \
                    <div class=\"modal-footer\"> \
                        <button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\"> \
                        Close \
                        </button> \
                    </div>" % (title, content)
    return HttpResponse(model_content)

@csrf_exempt
def searchMovieList(request, name, page="1"):
    webURL = "http://www.rs05.com/key/%s/%s" % (name, page)
    webURL = webURL.encode('utf-8')
    data = doGetList(webURL, page)
    return HttpResponse(data)

@csrf_exempt
def tagMovieList(request, name, page="1"):
    webURL = "http://www.rs05.com/tag/%s/%s" % (name, page)
    webURL = webURL.encode('utf-8')
    data = doGetList(webURL, page)
    return HttpResponse(data)
