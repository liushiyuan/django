from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import urllib
import re
import json
# Create your views here.

@csrf_exempt
def doPost(request):
    result = "nothing"
    if request.method == "POST":
        request_content = request.POST['url']
        request_content = request_content.encode('utf-8')
        request_type = request.POST['type']
        if request_type == "page":
            result = doPage(request_content)
            return HttpResponse(result)
        if request_type == "url":
            result = doURL(request_content)
            return HttpResponse(result)
        try:
            url = request_content.split("www.verycd.com")[1]
            keyword = None
        except Exception, e:
            keyword = request_content
            url = None
        if url:
            url = "http://www.verycd.gdajie.com" + url
            result = doURL(url)
        if keyword:
            result = doKeyword(keyword)
    return HttpResponse(result)

def doURL(url):
    result = ""
    try:
        response = urllib.urlopen(url)
        result = response.read()
        content = result.split("id=\"emuleFile\">")[1]
        content = content.split("</table>")[0]
        urls = re.findall('href="(.*)"', content)
        for url in urls:
            response = urllib.urlopen(url)
            result = response.read()
            ed2k = re.findall('ed2k(.*)"', result)
            ed2k = "ed2k" + ed2k[0]
            content = content.replace(url, ed2k)
        data = {"style":"single", "content":content}
        result = json.dumps(data)
    except Exception, e:
        data = {"error":str(e), "result":"failed"}
        result = json.dumps(data)
    return result

def doKeyword(keyword):
    url = "http://verycd.gdajie.com/find.htm?keyword=%s" % keyword
    return doPage(url)

def doPage(url):
    result = ""
    try:
        response = urllib.urlopen(url)
        result = response.read()
        pager = result.split("<div class=\"pager\">")[1]
        (pager, content) = (pager.split("<ul>")[0], pager.split("<ul>")[1])
        pager = re.findall('page=(\d+)', pager)
        try:
            page_num = pager[-2]
        except Exception, e:
            page_num = 1
        content = content.split("</ul>")[0]
        data = {"style":"list", "content":content, "lastpage":page_num, "result":"ok", "url":url}
        result = json.dumps(data)
    except Exception, e:
        data = {"error":str(e), "result":"failed"}
        result = json.dumps(data)
    return result

