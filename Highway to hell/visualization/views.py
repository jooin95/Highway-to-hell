from json import encoder
from django.shortcuts import render
from .ldafile import lda, correlation
from django.http import JsonResponse
import subprocess
import json
from urllib import parse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, timedelta
import time
import pymysql
from traceback import format_exc

myNaverKey1 = "x2i0xjwran"
myNaverKey2 = "ced9h4Hk4cUKJmCqa2QcUV3Ows7I0byrLEogtWdr"


def checkuser(request):
    if request.method == 'POST':
        startDate = request.POST['startDate']
        start_point = request.POST['start_point']
        finish_point = request.POST['finish_point']
        test1 = parse.quote_plus(start_point)
        test2 = parse.quote_plus(finish_point)
        cmd = ['curl',
               'https://naveropenapi.apigw.ntruss.com/map-place/v1/search?query=' +
               test1 + '&coordinate=127.1026513,37.2654939',
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
    cmd = ['curl',
           'https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start='
           + place1X + ',' + place1Y + '&goal=' + place2X + ',' + place2Y +
           '&option=trafast', '-H', 'X-NCP-APIGW-API-KEY-ID:' + myNaverKey1, '-H',
           'X-NCP-APIGW-API-KEY:' + myNaverKey2, '-v'
          ]
    f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
    data = f.read().strip()
    f.close()
    # data = json.dumps(data, cls=DjangoJSONEncoder)
    return JsonResponse({"data": data})


@csrf_exempt
def test_analysis(request):
    data = request.POST["data"]
    start = request.POST["startDate"].split()

    section = data['route']['trafast'][0]['section']
    guide = data['route']['trafast'][0]['guide']

    startNal = start[0].split('-')
    startTime = start[1].split(':')

    startYear = int(startNal[0])
    startMonth = int(startNal[1])
    startDate = int(startNal[2])
    startHour = int(startTime[0])
    startMin = int(startTime[1])
    startDay = datetime.date(startYear,startMonth,startDate).weekday()

    db = pymysql.connect("localhost", "root", "1234", "highwaytohell", charset="utf8")
    nowtime = datetime.utcnow() + timedelta(hours=9)

    nowMin = int(nowtime.strftime("%M"))
    nowHour = int(nowtime.strftime("%H"))
    nowYear = int(nowtime.strftime("%Y"))
    nowMonth = int(nowtime.strftime("%m"))
    nowDate = int(nowtime.strftime("%d"))
    nowDay = nowtime.weekday()

    try:
        cursor = db.cursor()
        sql = "select date, time from way1"
        cursor.execute(sql)
        times = cursor.fetchall()
    except IndexError:
        print(format_exc())
    finally:
        db.close()

    return JsonResponse({"data": data})