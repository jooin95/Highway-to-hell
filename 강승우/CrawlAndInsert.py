#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime, timedelta
import time
import pymysql
from traceback import format_exc


base_url = []
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EA%B2%BD%EB%B6%80%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EA%B2%BD%EC%9D%B8%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EA%B3%A0%EC%B0%BD%EB%8B%B4%EC%96%91%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EA%B4%91%EC%A3%BC%EB%8C%80%EA%B5%AC%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EA%B4%91%EC%A3%BC%EC%9B%90%EC%A3%BC%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%82%A8%ED%95%B4%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%88%9C%EC%B2%9C-%EB%B6%80%EC%82%B0)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%82%A8%ED%95%B4%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%98%81%EC%95%94-%EC%88%9C%EC%B2%9C)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%82%A8%ED%95%B4%EC%A0%9C1%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%EC%A7%80%EC%84%A0%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%85%BC%EC%82%B0%EC%B2%9C%EC%95%88%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8B%B9%EC%A7%84%EC%98%81%EB%8D%95%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EB%8C%80%EC%A0%84-%EB%8B%B9%EC%A7%84)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8B%B9%EC%A7%84%EC%98%81%EB%8D%95%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%83%81%EC%A3%BC-%EC%98%81%EB%8D%95)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8B%B9%EC%A7%84%EC%98%81%EB%8D%95%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%B2%AD%EC%A3%BC-%EC%83%81%EC%A3%BC)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8C%80%EC%A0%84%EB%82%A8%EB%B6%80%EC%88%9C%ED%99%98%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8F%99%ED%95%B4%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EB%B6%80%EC%82%B0-%EC%9A%B8%EC%82%B0)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8F%99%ED%95%B4%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%82%BC%EC%B2%99-%EC%86%8D%EC%B4%88)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%8F%99%ED%95%B4%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%9A%B8%EC%82%B0-%ED%8F%AC%ED%95%AD)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%AC%B4%EC%95%88%EA%B4%91%EC%A3%BC%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B6%80%EC%82%B0%EC%99%B8%EA%B3%BD%EC%88%9C%ED%99%98%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%83%81%EC%A3%BC%EC%98%81%EC%B2%9C%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%84%9C%EC%9A%B8%EC%96%91%EC%96%91%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%84%9C%EC%9A%B8%EC%99%B8%EA%B3%BD%EC%88%9C%ED%99%98%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%84%9C%EC%B2%9C%EA%B3%B5%EC%A3%BC%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%84%9C%ED%95%B4%EC%95%88%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%84%B8%EC%A2%85%ED%8F%AC%EC%B2%9C%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EA%B5%AC%EB%A6%AC-%ED%8F%AC%EC%B2%9C)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%84%B8%EC%A2%85%ED%8F%AC%EC%B2%9C%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%96%91%EC%A3%BC-%EC%86%8C%ED%9D%98)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%88%98%EB%8F%84%EA%B6%8C%EC%A0%9C2%EC%88%9C%ED%99%98%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EB%B4%89%EB%8B%B4-%EB%8F%99%ED%83%84)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%88%98%EB%8F%84%EA%B6%8C%EC%A0%9C2%EC%88%9C%ED%99%98%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%9D%B8%EC%B2%9C-%EA%B9%80%ED%8F%AC)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%88%9C%EC%B2%9C%EC%99%84%EC%A3%BC%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%95%84%EC%82%B0%EC%B2%AD%EC%A3%BC%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%98%A5%EC%82%B0-%EC%98%A4%EC%B0%BD)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%98%81%EB%8F%99%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%9A%A9%EC%9D%B8%EC%84%9C%EC%9A%B8%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%9A%B8%EC%82%B0%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%9D%B5%EC%82%B0%ED%8F%AC%ED%95%AD%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EB%8C%80%EA%B5%AC-%ED%8F%AC%ED%95%AD)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%9D%B5%EC%82%B0%ED%8F%AC%ED%95%AD%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%9D%B5%EC%82%B0-%EC%9E%A5%EC%88%98)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%9D%B8%EC%B2%9C%EA%B5%AD%EC%A0%9C%EA%B3%B5%ED%95%AD%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")

base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%9C2%EA%B2%BD%EC%9D%B8%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%86%A1%EB%8F%84-%EC%97%B0%EC%88%98)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%9C2%EA%B2%BD%EC%9D%B8%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%95%88%EC%96%91-%EC%84%B1%EB%82%A8)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%9C2%EA%B2%BD%EC%9D%B8%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%9D%B8%EC%B2%9C%EB%8C%80%EA%B5%90)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%9C2%EA%B2%BD%EC%9D%B8%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")

base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%9C2%EC%A4%91%EB%B6%80%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A4%91%EB%B6%80%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A4%91%EB%B6%80%EB%82%B4%EB%A5%99%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A4%91%EC%95%99%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EB%B6%80%EC%82%B0-%EB%8C%80%EA%B5%AC)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A4%91%EC%95%99%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%82%BC%EB%9D%BD-%EB%8C%80%EB%8F%99)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A4%91%EC%95%99%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%B6%98%EC%B2%9C-%EA%B8%88%ED%98%B8)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%86%B5%EC%98%81%EB%8C%80%EC%A0%84%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%8F%89%ED%83%9D%EC%8B%9C%ED%9D%A5%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%8F%89%ED%83%9D%EC%A0%9C%EC%B2%9C%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%8F%89%ED%83%9D%ED%8C%8C%EC%A3%BC%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%EC%88%98%EC%9B%90-%EA%B4%91%EB%AA%85)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%8F%89%ED%83%9D%ED%8C%8C%EC%A3%BC%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C(%ED%8F%89%ED%83%9D-%ED%99%94%EC%84%B1)%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%98%B8%EB%82%A8%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")
base_url.append("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%ED%98%B8%EB%82%A8%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C%EC%A7%80%EC%84%A0%20%EA%B5%90%ED%86%B5%EC%A0%95%EB%B3%B4")

db = pymysql.connect("localhost","root","1234","highwaytohell",charset="utf8")

while(1):
	nowtime = datetime.utcnow() + timedelta(hours=9)
	if int(nowtime.strftime("%M"))%10 == 0:
		try:

			cursor = db.cursor()



			sql = "select * from highways order by ordernumber"
			cursor.execute(sql)
			highwayall = cursor.fetchall()

			insertion = []
			i=0
			for ways in highwayall:
				response = urlopen(base_url[i])
				html = response.read()
				soup = BeautifulSoup(html,"html.parser",from_encoding='utf-8')
				insertion.append("insert into way")
				insertion[i] += str(i+1) + "(date, time"
				for k in range(0, ways[2]-1):
					insertion[i] += ",h"+str(k+1)+"_h"+str(k+2)
				for k in range(ways[2], 1, -1):
					insertion[i] += ",h"+str(k)+"_h"+str(k-1)
				insertion[i] += ") values(" + nowtime.strftime("%Y-%m-%d") +"," + nowtime.strftime("%H:%M:%S")
				for k in range(ways[2]-1):
					roadrange = ways[3+k] + "~" + ways[4+k]
					strResult = soup.find("a",text=roadrange).findNext('dd').findNext('dd').text
					token = strResult.split()
					timeResult = token[1].replace("분","")
					insertion[i] += ","+ timeResult
				for k in range(ways[2]-1, 0, -1):
					roadrange = ways[3+k] + "~" + ways[2+k]
					strResult = soup.find('a',text=roadrange).findNext('dd').findNext('dd').text
					token = strResult.split()
					timeResult = token[1].replace("분","")
					insertion[i] += ","+ timeResult
				insertion[i] += ")"
				i = i+1
			for i in range(0,52):
				cursor.execute(insertion[i])
			db.commit()
			print("complete insertion at :"+nowtime.strftime("%Y-%m-%d") +"," + nowtime.strftime("%H:%M:%S"))
		except IndexError:
			print(format_exc())

		finally:
			db.close()
	time.sleep(60000)
