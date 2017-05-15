#gamestate.h
import sys
import os

sys.path.append(os.path.abspath("../inputs"))
from keyboard_mouse import *

sys.path.append(os.path.abspath("../player"))
from player import *

sys.path.append(os.path.abspath("../map"))
from gamemap import *

sys.path.append(os.path.abspath("../objects"))
from object_set import *

sys.path.append(os.path.abspath("../menu"))
from menus import *

sys.path.append(os.path.abspath("../draw"))
from drawutils import *

EXIT = 0
RETURN = 1
KEEPOPEN = 3

class Gamestate:
	def __init__(self, inputs):
		self._inputs = inputs;
		self.ingame = False
		self.menuopen = True
		self.open_menu()


	def change_state(self):
		print ("Change State")
		self.ingame = not self.ingame;
		if self.ingame:
			#TODO: CHANGE TO SET_LEVEL
			#gamemap = Basic_Gamemap()
			#self.set_level(gamemap)
			#---PERMANENT ABOVE---
			#---TEMPORARY BELOW---
			self.set_test_level()

	def set_test_level(self):		
		self.gamemap = Basic_Gamemap()
		self.player = Player()
		self.objects = Object_Set(self.gamemap)
	
	def set_level(self, gamemap):
		if self.ingame == True:
			self.gamemap = Gamemap(gamemap)
			self.player = Player()
			self.objects = Object_Set(self.gamemap)
			self.debug = False

	def open_menu(self):
		self.menuopen = True
		if (self.ingame):
			self.menu = Ingame_Menu()
			print("Open Menu -- Out of game")
		else:
			#Set up main menu:
			self.menu = Main_Menu()
			print("Open Menu -- ingame")

	def menu_state(self):
		#if condtioions are right, close menu.
		#Determine how
		return self.menu.get_state()
		

		#Potential errors in update so WATCHOUT

	def update(self):
		self._inputs.update()
		#what to do in the game:
		if self.ingame:
			if self.menuopen == True:
				self.menu.update()
				if (self.menu_state == "EXIT"):
					self.change_state()
					self.menuopen = False

		
			if self._inputs.ispressed("MENU"):
				self.open_menu()
			#Update player:
			self.player.update(self._inputs, self.gamemap, self.objects)
			#Update map:
			self.objects.update(self.player, self.gamemap)
			#Update drawing
		else:
			self.menu.update()
			if (self.menu_state() == "START"):
				self.change_state()
				self.menuopen = False

	def draw(self, drawutils, screen):
		if self.ingame:
			self.draw_ingame(drawutils, screen)
		else:
			self.draw_outgame(drawutils, screen)

	def draw_ingame(self, drawutils, screen):
		print "Ingame"	

	def draw_outgame(self, drawutils, screen):
		self.menu.draw(drawutils, screen)
