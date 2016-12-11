from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import urllib
import re
import json
import os
# Create your views here.

DomainName = "www.bthit.com"

@csrf_exempt
def doPost(request):
    result = "nothing"
    if request.method == "POST":
        request_content = request.POST['value']
        request_content = request_content.encode('utf-8')
        request_type = request.POST['type']
        if request_type == "search":
            webURL = "http://%s/list/%s-s1d-1.html" % (DomainName, request_content)
            result = doSearch(webURL)
        if request_type == "page":
            page = request.POST['pagenum']
            page =  page.encode('utf-8')
            webURL = "http://%s/list/%s-s1d-%s.html" % (DomainName, request_content, page)
            result = doSearch(webURL)
        if request_type == "detail":
            result = doGetDetail(request_content)
    return HttpResponse(result)

def doSearch(webURL):
    pagenum = ""
    try:
        response = os.popen("curl -s --compressed \"%s\"" % (webURL))
        result = response.read()
        content = result.split("<ul class=\"mlist\">")
        content[0] = ""
        pagenum = content[-1].split("class=\"flag_pg\"")
        content[-1] = content[-1].split("<div id=\"mpages\">")[0]
        if (len(pagenum) > 1):
            pagenum = pagenum.split("s1d-")[-1]
            pagenum = pagenum.split(".")[0]
        else:
            pagenum = "1"
        mystr = "<ul class=\"mlist\">";
        data = {"content":mystr.join(content), "pagenum":pagenum, "result":"ok"}
    except Exception, e:
        data = {"content":str(e), "result":"error"}
    result = json.dumps(data)
    return result

def doGetDetail(url):
    url = url.split("/")[-1]
    webURL = "http://%s/info/%s" % (DomainName, url)
    try:
        response = os.popen("curl -s --compressed \"%s\"" % (webURL))
        result = response.read()
        magnet = result.split("magnet:")[1]
        magnet = "magnet:%s" % magnet.split("\"")[0]
        thunder = result.split("thunder:")[1]
        thunder = "thunder:%s" % thunder.split("\"")[0]
        data = {"magnet":magnet, "thunder":thunder, "result":"ok"}
    except Exception, e:
        data = {"content":str(e), "result":"error"}
    result = json.dumps(data)
    return result
