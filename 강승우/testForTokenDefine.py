#-*- coding: utf-8 -*-
import pymysql
from traceback import format_exc
from json import encoder
from django.shortcuts import render
import json
from django.core.serializers.json import DjangoJSONEncoder
from urllib import parse
import subprocess

db = pymysql.connect("localhost","root","1234","highwaytohell",charset="utf8")
myNaverKey1 = "x2i0xjwran"
myNaverKey2 = "ced9h4Hk4cUKJmCqa2QcUV3Ows7I0byrLEogtWdr"


try:
	token = '청주분기점'
	cursor = db.cursor()

	sql = "select * from place"
	cursor.execute(sql)
	places = cursor.fetchall()
	
	cmd = ['curl',
	   'https://naveropenapi.apigw.ntruss.com/map-place/v1/search?query=' +
	   parse.quote_plus(token) + '&coordinate=127.1026513,37.2654939',
	   '-H', 'X-NCP-APIGW-API-KEY-ID:' + myNaverKey1, '-H',
	   'X-NCP-APIGW-API-KEY:' + myNaverKey2, '-v'
	   ]
	f = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding="utf-8").stdout
	data1 = f.read().strip()
	f.close()
	data = json.loads(data1)
	lng = float(data['places'][0]['x'])
	lat = float(data['places'][0]['y'])
	
	CurID = ""
	newID = ""
	CurCom = 0.0
	newCom = 0.0
	for row in places:
		if CurID == "" :
			CurID = row[0]
			CurCom = abs((lng + lat - row[1] - row[2])**2)
		else:
			newID = row[0]
			newCom = abs((lng + lat - row[1] - row[2])**2)
			if newCom < CurCom :
				CurCom = newCom
				CurID = newID
	print(CurCom)
	way = CurID.split('h')
	sql = "select * from highways where ID = '" + way[0] + "';"
	cursor.execute(sql)
	highway = cursor.fetchall()
	maintoken = highway[0][2+int(way[1])]
	
	sql = "select * from place where ID ='"+CurID+"'"
	cursor.execute(sql)
	places = cursor.fetchall()
	CurLng = places[0][1]
	CurLat = places[0][2]
	
	sql = "select * from place where lng = "+ format(CurLng,'12.8f') + " and lat = " + format(CurLat,'12.8f') + ";" 
	cursor.execute(sql)
	places = cursor.fetchall()
	
	ways = []
	tokens = []
	
	for row in places:
		hightoken = (row[0].split('h'))[0]
		ways.append(hightoken)
		tokens.append("h"+(row[0].split('h'))[1])
	
	print (maintoken)
	print (tokens)
	print (ways)
	Jways = "{ 'token' : ["
	for row in tokens:
		Jways += "'"+row+"',"
	Jways.rstrip(',')
	Jways.rstrip(',')
	Jways+="],"
	Jways += "'highways' : ["
	for row in ways:
		Jways += "'"+row+"',"
	Jways.rstrip(',')
	Jways.rstrip(',')
	Jways+="]}"
	print (Jways)
	rec = json.loads(Jways)
	print (rec)
except IndexError:
	print(format_exc())

finally:
	db.close()
