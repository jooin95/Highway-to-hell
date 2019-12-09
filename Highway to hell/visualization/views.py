from json import encoder
from django.shortcuts import render
from .ldafile import lda, correlation
from django.http import JsonResponse
import subprocess
import json
from datetime import datetime, timedelta
from urllib import parse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import time
from django.db import connection
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
    print(data)
    return JsonResponse({"data": data})


@csrf_exempt
def test_analysis(request):
    a = 0
    data1 = request.POST["data1"]
    data2 = request.POST["data2"]
    data3 = request.POST["data3"]
	
    type = request.POST.get('guide1','')
    duration = request.POST.get('guide2','')
    print(type)
    startDate = request.POST["startDate"]
    Date = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S').date()
    Time = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S').time()
    before = Date - timedelta(3)
    after = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S') + timedelta(hours=3)
    after = after.time()
    data = [data1, data2, data3]
    print(data)
    select = []
    for d in data:
        cursor = connection.cursor()
        cur = connection.cursor()
        query_string = "select ID, num from highways where name = %s;"
        cursor.execute(query_string, d)
        row = cursor.fetchall()
        collect = []
        print(row)
        if(row):
            string = "select * from " + row[0][0] + " where date >= %s AND time >= %s AND time <= %s;"
            cur.execute(string, (before, Time, after))
            rs = cur.fetchall()
            b = 0
            for r in rs:
                sum1 = 0
                sum2 = 0
                for i in range(2, row[0][1] + 1):
                    sum1 = sum1 + r[i]
                for i in range(row[0][1] + 2, 2 * (row[0][1] - 1) + 2):
                    sum2 = sum2 + r[i]
                dic = {
                    'index': b,
                    'Date': r[0],
                    'Time': r[1],
                    '정방향': sum1,
                    '역방향': sum2
                }
                b = b + 1
                collect.append(dic)
                print(collect)
        dict = {
            'name': data[a],
            'TfD': collect
        }
        select.append(dict)

        a = a + 1
    print(select)
    final = select
    final = json.dumps(final, cls=DjangoJSONEncoder, ensure_ascii=False)
    return JsonResponse({"select": select})

