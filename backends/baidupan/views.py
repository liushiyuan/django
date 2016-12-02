from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import urllib
import re
import json
import os
# Create your views here.

DomainName = "www.wangpansou.cn"

@csrf_exempt
def doPost(request):
    result = "nothing"
    if request.method == "POST":
        request_content = request.POST['value']
        request_content = request_content.encode('utf-8')
        request_type = request.POST['type']
        if request_type == "search":
            webURL = "http://%s/s.php?q=%s&wp=15&start=0" % (DomainName, request_content)
            result = doSearch(webURL)
        if request_type == "page":
            page = request.POST['pagenum']
            page = int(page)
            page = (page - 1) * 10
            page = str(page)
            page =  page.encode('utf-8')
            webURL = "http://%s/s.php?q=%s&wp=15&start=%s" % (DomainName, request_content, page)
            result = doSearch(webURL)
    return HttpResponse(result)

def doSearch(webURL):
    pagenum = ""
    try:
        response = os.popen("wget -qO- \"%s\"" % (webURL))
        result = response.read()
        content = result.split("<div class=\"cse-search-result_content_item\">")
        content[0] = ""
        pagenum = content[-1].split("<div class=\"cse-search-result_top_line\"")[1]
        content[-1] = content[-1].split("<div class=\"cse-search-result_top_line\"")[0]
        pagenum = pagenum.split("tabindex=\"")
        pagenum = pagenum[-1].split("\"")[0]
        data = {"content":content, "pagenum":pagenum, "result":"ok"}
    except Exception, e:
        data = {"content":str(e), "result":"error"}
    result = json.dumps(data)
    return result
