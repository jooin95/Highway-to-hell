#-*- coding: utf-8 -*-
import pymysql
from traceback import format_exc
from json import encoder
from django.shortcuts import render
import json
from django.core.serializers.json import DjangoJSONEncoder

db = pymysql.connect("localhost","root","1234","highwaytohell",charset="utf8")
myNaverKey1 = "x2i0xjwran"
myNaverKey2 = "ced9h4Hk4cUKJmCqa2QcUV3Ows7I0byrLEogtWdr"


try:

	cursor = db.cursor()

	sql = "select * from highways order by ordernumber"
	cursor.execute(sql)
	highwayall = cursor.fetchall()
	
	insertion = []
	k=0
	for row in highwayall:
		i = 3
		for high in row:
			if i-2 > row[2]:
				break
			insertion.append("insert into place values('")
			insertion[k] += row[0] + "h" + (i-2)+"',"
			cmd = ['curl',
               'https://naveropenapi.apigw.ntruss.com/map-place/v1/search?query=' +
               parse.quote_plus(high) + '&coordinate=127.1026513,37.2654939',
               '-H', 'X-NCP-APIGW-API-KEY-ID:' + myNaverKey1, '-H',
               'X-NCP-APIGW-API-KEY:' + myNaverKey2, '-v'
               ]
			f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
			data1 = f.read().strip()
			f.close()
			data1 = json.dumps(data1, cls=DjangoJSONEncoder)
			insertion[k] += data1['places'][0]['x']+ "," + data1['places'][0]['y'] + ");"
			i += 1
		k += 1
	
	for i in insertion:
		print(i)
except IndexError:
	print(format_exc())

finally:
	db.close()
