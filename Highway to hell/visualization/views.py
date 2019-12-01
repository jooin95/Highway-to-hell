from django.shortcuts import render
from .models import TrendWithSales, TrendWithItemFreq, keyword_insert, topic_class,practice, publish_onion
from .ldafile import lda, correlation
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.db.models import Q, F, Value
from django.db.models.functions import Concat
from django.db import connection
from datetime import datetime, timedelta
from django.db.models import Avg, Sum, Count
import time
import json
import pandas as pd
from pymongo import MongoClient
import pandas as pd
import numpy as np
from functools import reduce
import operator
#from konlpy.tag import Kkma # 형태소분석기를 만들기 위해서 설정함.
from collections import Counter # Counter생성함.
# from konlpy.tag import Hannanum # 형태소분석기를 만들기 위해서 설정함.
import operator # dictionary를 정렬하기 위해서 구현함.
from collections import defaultdict

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
    sel_list = {
        'startDate': startDate,
        'start_point': start_point,
        'finish_point': finish_point,
    }
    print(startDate)
    print(start_point)
    print(finish_point)
    # cursor = connection.cursor()
    # print(startDate)
    # query_string = "SELECT GetDT, ElePower, Ampere, Voltage, CastSpeed," \
    #                "Frequency FROM TP_MDF_GETDATA " \
    #                "where GetDT >=%s LIMIT 100;"
    # cursor.execute(query_string, startDate)
    # rows = cursor.fetchall()
    # data_list = []
    # for row in rows:
    #     # date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').date()
    #     dic = {
    #         'GetTime': row[0],
    #         'ElePower': row[1],
    #         'Ampere': row[2],
    #         'Voltage': row[3],
    #         'CastSpeed': row[4],
    #         'Frequency': row[5]
    #     }
    #     data_list.append(dic)
    # data_list = json.dumps(data_list, cls=DjangoJSONEncoder)
    return JsonResponse({"Sel_list": sel_list})
