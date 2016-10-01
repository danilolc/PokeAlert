#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Este é o arquivo principal

from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from gi.repository import Gtk as gtk
from datetime import datetime
import thread
import signal
import time
import os

import pokesound
import pokedata

APPINDICATOR_ID = 'pokealert'

pokemon = pokedata.Pokedata()

icon1 = pokedata.MAIN_PATH + 'poke.png'
icon2 = pokedata.MAIN_PATH + 'pokes.png'

class App(object):
	
	def __init__(self):
		self.indicator = appindicator.Indicator.new(
			APPINDICATOR_ID, 
			os.path.abspath(icon1), 
			appindicator.IndicatorCategory.SYSTEM_SERVICES)
		self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
		self.indicator.set_menu(self.build_menu())
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		notify.init(APPINDICATOR_ID)
		thread.start_new_thread(self.updater,())
		gtk.main()

	def build_menu(self):
		self.item_srch = gtk.MenuItem('Pesquisar')
		self.item_srch.connect('activate', self.reupdate)

		
		item_quit = gtk.MenuItem('Sair')
		item_quit.connect('activate', self.quit)

		menu = gtk.Menu()
		menu.append(self.item_srch)
		
		menu.append(gtk.SeparatorMenuItem())

		self.mens = gtk.MenuItem('Sem Pokémon proximos')
		self.mens.set_sensitive(False)
		menu.append(self.mens)

		menu.append(gtk.SeparatorMenuItem())
		
		menu.append(item_quit)
		menu.show_all()

		return menu

	def reupdate(self,source):
		pass

	def updater(self):
		while True:
			print("Atualizou")
			thread.start_new_thread(pokemon.updatedata,())
			self.indicator.set_icon(os.path.abspath(icon2))
			self.item_srch.set_sensitive(False)
			self.item_srch.set_label("Pesquisando...")

			while pokemon.runing==False:
				pass 
			while pokemon.runing==True:
				pass
			#pokesound.play("1")

			self.indicator.set_icon(os.path.abspath(icon1))
			self.item_srch.set_label("Pesquisar")
			self.item_srch.set_sensitive(True)
			try:
				print pokemon.data
				self.mens.set_label("Pokémon próximos")
			except:
				self.mens.set_label("Sem Pokémon proximos")

			time.sleep(120)

	def quit(self,source):
		gtk.main_quit()

if __name__ == "__main__":
	app = App()
