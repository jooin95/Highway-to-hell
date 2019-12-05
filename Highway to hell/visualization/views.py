from json import encoder
from django.shortcuts import render
from .models import TrendWithSales, TrendWithItemFreq, keyword_insert, topic_class,practice, publish_onion
from .ldafile import lda, correlation
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
import subprocess
from urllib import parse
from django.views.decorators.csrf import csrf_exempt

from django.core.serializers.json import DjangoJSONEncoder


def underDev(request):
    return render(request, 'underdev/underdev.html')


def test3(request):
    return render(request, "test/test3.html")

@csrf_exempt
def test_send(request):
    startDate = request.POST['StartDate']
    start_point = request.POST['start_point']
    finish_point = request.POST['finish_point']
    test1 = parse.quote_plus(start_point)
    test2 = parse.quote_plus(finish_point)
    cmd = ['curl',
           'https://naveropenapi.apigw.ntruss.com/map-place/v1/search?query=' +
           test1 + '&coordinate=127.1054328,37.3595963',
           '-H', 'X-NCP-APIGW-API-KEY-ID:x2i0xjwran', '-H',
           'X-NCP-APIGW-API-KEY:ced9h4Hk4cUKJmCqa2QcUV3Ows7I0byrLEogtWdr', '-v'
          ]
    f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
    data1 = f.read().strip()
    f.close()
    cmd = ['curl',
           'https://naveropenapi.apigw.ntruss.com/map-place/v1/search?query=' +
           test2 + '&coordinate=127.1054328,37.3595963',
           '-H', 'X-NCP-APIGW-API-KEY-ID:x2i0xjwran', '-H',
           'X-NCP-APIGW-API-KEY:ced9h4Hk4cUKJmCqa2QcUV3Ows7I0byrLEogtWdr', '-v'
           ]
    f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
    data2 = f.read().strip()

    sel_list = {
        'startDate': startDate,
        'start_point': start_point,
        'finish_point': finish_point,
    }
    print(data1)
    print(data2)
    return JsonResponse({"data1": data1, "data2": data2, "startDate": startDate})
