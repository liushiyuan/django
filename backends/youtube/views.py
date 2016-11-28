from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import base64
import httplib
import urllib
# Create your views here.

@csrf_exempt
def doPost(request):
    video_url = "bad url"
    if request.method == "POST":
        params = urllib.urlencode({'urlb64': base64.b64encode(request.POST['url'])})
        headers = {"Host": "98.126.14.234",
				"Connection": "keep-alive",
				"Content-Length": len(params),
				"Origin": "http://98.126.14.234",
				"X-Requested-With": "XMLHttpRequest",
				"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
				"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
				"Accept": "text/plain,*/*;q=0.01",
				"Referer": "http://98.126.14.234/",
				"Accept-Encoding": "gzip,deflate",
				"Accept-Language": "zh-CN,zh;q=0.8"}
        try:
            conn = httplib.HTTPConnection("98.126.14.234", 80)
            conn.request("POST", "/system/proceed.php", params, headers)
            response = conn.getresponse()
            if response.status == 200:
                video_url = response.read().split("\"")[1]
                video_url = video_url.replace("..", "http://98.126.14.234")
            else:
                video_url = "bad url"
            conn.close()
        except Exception, e:
            video_url = "bad url"
    return HttpResponse(video_url)
