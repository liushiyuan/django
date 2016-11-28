from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import urllib
import re
import json
import os
from StringIO import StringIO
import gzip
import httplib
# Create your views here.

@csrf_exempt
def doPost(request):
    result = "nothing"
    if request.method == "POST":
        request_content = request.POST['value']
        request_content = request_content.encode('utf-8')
        request_type = request.POST['type']
        if request_type == "google":
            result = doGoogle(request_content)
        if request_type == "pdfpage":
            result = doPdfpage(request_content)
    return HttpResponse(result)

def doPdfpage(value):
    params = urllib.urlencode({'url':value})
    headers = {"Host": "www.htm2pdf.co.uk",
	"Connection": "keep-alive",
	"Content-Length": len(params),
	"Origin": "http://www.htm2pdf.co.uk",
	"X-Requested-With": "XMLHttpRequest",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Accept": "text/plain,*/*;q=0.01",
	"Referer": "http://www.htm2pdf.co.uk/",
	"Accept-Encoding": "gzip,deflate",
	"Accept-Language": "zh-CN,zh;q=0.8"}
    try:
        conn = httplib.HTTPConnection("www.htm2pdf.co.uk", 80)
        conn.request("POST", "/convert_url.php", params, headers)
        response = conn.getresponse()
        if response.status == 200:
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            content = f.read()
            content = content.split('/')[1]
            content = content.split('>')[0]
            content = "http://www.htm2pdf.co.uk/%s" % content
            data = {"style":"pdfpage", "content":content, "result":"ok"}
        else:
            data = {"error":response.status, "result":"failed"}
    except Exception, e:
        data = {"error":str(e), "result":"failed"}
    result = json.dumps(data)
    return result

def doGoogle(value):
    try:
        fd = os.popen("googler \"%s\" -n 50 --json" % value)
        data = {"style":"google", "content":fd.read(), "result":"ok"}
    except Exception, e:
        data = {"error":str(e), "result":"failed"}
    result = json.dumps(data)
    return result
    
