#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Notify as notify
import time
import os

import pokefinder

#Diretório do PokeAlert
MAIN_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
print (MAIN_PATH)

#Coloque as coordenadas
lat = -19.9321203
lgt = -43.9379854

class Pokedata(object):
	runing = False
	pokes = 0
	data = object
	
	def __init__(self):
		pass

	def alert(self,numb,mi,sc):
		name = self.getname(numb)
		img = str(numb)
		if numb<10:
			img = '00' + img
		elif numb<100:
			img = '0' + img
		message = '<b>Tem um ' + name + ' próximo</b>'
		path = MAIN_PATH + 'spr/' + img + '.png'
		n = notify.Notification.new(message, str(mi) + "\' " + str(sc) + "\'\'", os.path.abspath(path))
		n.show()

	def getname(self,numb):
		file = open("list.txt","r")
		name = file.readlines()[numb]
		name = name.replace("_female", "♀")
		name = name.replace("_male", "♂")
		name = name.replace("\n","")
		file.close()
		return name

	def getno(self,pokemon):
		pokemon = pokemon.capitalize()
		file = open("list.txt","r")
		for i,line in enumerate(file):
			line = line.decode('utf-8')
			if pokemon+"\n" in line:
				return i
		return 0

	def updatedata(self):
		self.runing = True
		while True:
			data = pokefinder.getdata(lat,lgt)
			try:
				self.data = data.result
				print("Sucesso")
				break
			except:
				print("Erro")

				time.sleep(0.5)
		self.pokes = len(self.data)
		self.runing = False
		#--
		for x in range(0, self.pokes):
			self.alert(self.getno(self.data[x].pokemon_id),1,2)
		#spawn_point_id #encounter_id #pokemon_id #expiration_timestamp_ms #latitude #longitude
		#PKM Number, Spawn Point, Expiration
