from json import encoder
from django.shortcuts import render
from .ldafile import lda, correlation
from django.http import JsonResponse
import subprocess
import json
from urllib import parse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
myNaverKey1 = "네이버 첫번쨰 키"
myNaverKey2 = "네이버 두번쨰 키"


def checkuser(request):
    if request.method == 'POST':
        startDate = request.POST['startDate']
        start_point = request.POST['start_point']
        finish_point = request.POST['finish_point']
        test1 = parse.quote_plus(start_point)
        test2 = parse.quote_plus(finish_point)
        cmd = ['curl',
               'https://naveropenapi.apigw.ntruss.com/map-place/v1/search?query=' +
               test1 + '&coordinate=127.1054328,37.3595963',
               '-H', 'X-NCP-APIGW-API-KEY-ID:' + myNaverKey1, '-H',
               'X-NCP-APIGW-API-KEY:' + myNaverKey2, '-v'
               ]
        f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
        data1 = f.read().strip()
        f.close()
        cmd = ['curl',
               'https://naveropenapi.apigw.ntruss.com/map-place/v1/search?query=' +
               test2 + '&coordinate=127.1054328,37.3595963',
               '-H', 'X-NCP-APIGW-API-KEY-ID:' + myNaverKey1, '-H',
               'X-NCP-APIGW-API-KEY:' + myNaverKey2, '-v'
               ]
        f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
        data2 = f.read().strip()
        f.close()
        data1 = json.dumps(data1, cls=DjangoJSONEncoder)
        data2 = json.dumps(data2, cls=DjangoJSONEncoder)
        return render(request, 'test/visualize.html', {"data1": data1, "data2": data2, "startDate": startDate})
    elif request.method == 'GET':
        return render(request, "test/checkuser.html")


def visualize(request):
    return render(request, "test/visualize.html")


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
           '-H', 'X-NCP-APIGW-API-KEY-ID:' + myNaverKey1, '-H',
           'X-NCP-APIGW-API-KEY:' + myNaverKey2, '-v'
          ]
    f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
    data1 = f.read().strip()
    f.close()
    cmd = ['curl',
           'https://naveropenapi.apigw.ntruss.com/map-place/v1/search?query=' +
           test2 + '&coordinate=127.1054328,37.3595963',
           '-H', 'X-NCP-APIGW-API-KEY-ID:' + myNaverKey1, '-H',
           'X-NCP-APIGW-API-KEY:' + myNaverKey2, '-v'
           ]
    f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
    data2 = f.read().strip()
    f.close()
    return JsonResponse({"data1": data1, "data2": data2, "startDate": startDate})


@csrf_exempt
def test_visualize(request):
    place1X = request.POST['place1X']
    place1Y = request.POST['place1Y']
    place2X = request.POST['place2X']
    place2Y = request.POST['place2Y']
    startDate = request.POST['startDate']
    cmd = ['curl',
           'https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start='
           + place1X + ',' + place1Y + '&goal=' + place2X + ',' + place2Y +
           '&option=trafast', '-H', 'X-NCP-APIGW-API-KEY-ID:' + myNaverKey1, '-H',
           'X-NCP-APIGW-API-KEY:' + myNaverKey2, '-v'
          ]
    f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
    data = f.read().strip()
    print(data)
    f.close()
    return JsonResponse({"data": data, "startDate": startDate})