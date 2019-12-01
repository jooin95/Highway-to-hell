from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from datetime import datetime
from Highway_to_hell.models import Highway, UserWant
from Highway_to_hell.forms import CheckForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def index(request):
    return render(request, 'highway/index.html')

@csrf_exempt
def test_send(request):
    startDate = request.POST['StartDate']

    cursor = connection.cursor()
    print(startDate)
    query_string = ""
    cursor.execute(query_string, startDate)
    rows = cursor.fetchall()
    data_list = []
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
    # # data_list = json.dumps(data_list, cls=DjangoJSONEncoder)

    return JsonResponse({"data_list": data_list})