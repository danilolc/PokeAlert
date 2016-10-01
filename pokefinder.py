#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
from requests import Session
import json

connect = False

headers={'Host': 'api.fastpokemap.se', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding':'gzip,deflate,br','Origin':'https://fastpokemap.se',
'DTN':'1','Connection':'keep-alive'}

try:
	session = Session()
	session.head('https://fastpokemap.se')
	connect = True
except:
	print ("Erro na conecção")

def getdata(lat,lng):
	print ("Pegando dados")	
	try:
		data = session.post(
			url='https://api.fastpokemap.se/?key=allow-all&ts=0&lat=' + str(lat) + '&lng=' + str(lng),
			data={},
			headers=headers)
	except:
		return "Erro no pacote"
	data = json.loads(data.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
	return data
