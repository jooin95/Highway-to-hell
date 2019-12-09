# Highway-to-hell

How To Get Into Website

url: 34.232.249.58:8000 (elastic public IP)

Main Folder : ./Highway to hell

TO RUN SERVER : go into dir ./Highway to hell
				python3 manage.py runserver 0.0.0.0:8000
				
Introduction : This program is for expecting car travel time in the future.
			   Select start time you want to travel and this website will expect time based on crawled informations
			   This program crawl data of all real-time highway traffic informations in frequency of 10min
			   This program use Naver Map API for getting direction.

Crawling : aws ubuntu mysql python(beautifulsoup)



Web : aws ubuntu python Django



TO BUILD BACK GROUND

get clone of this github url

DOWNLOAD mysql, python3, beautifulsoup4, Django2.1

for libs in python, run this codes

$sudo apt install libpq-dev python-dev

$pip3 install django==2.1

$pip3 install django-cors-headers

$pip3 install django==2.1

$pip3 install djongo

$pip3 install django==2.1

$pip3 install jsonfield

$pip3 install django==2.1

$pip3 install psycopg2

$pip3 install django==2.1

$pip3 install gensim

$pip3 install konlpy

$pip3 install spacy

$pip3 install pandas

$pip3 install sklearn

$pip3 install nltk

$pip3 install pyLDAvis

if there are more libs needed, follow additional error codes



Database BuildUp

$mysql -uroot -p

set password as 1234

there are 3 txt files in ./강승우/DBbuildUpCodes
copy them to mysql

Crawling
run ./강승우/CrawlAndInsert.py by using command below


$python3 CrawlAndInsert.py


If you need to run it after exiting session, 
write command 


$screen -S session_name    >>>> session_name that you want

and run that command
When you want to get out of that session, Ctrl + a + d
Get into that session again by using command below when you need


$screen -r session_name


Refer to this page http://blog.naver.com/PostView.nhn?blogId=hyungjungkim&logNo=221329251023&categoryNo=43&parentCategoryNo=0
to get more information