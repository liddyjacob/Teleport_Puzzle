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
from objects import *

EXIT = 0
RETURN = 1
KEEPOPEN = 3

class Gamestate:
	def __init__(self, inputs):
		self._inputs = inputs;
		self.ingame = False
		self.menuopen = False


	def change_state(self):
		self.ingame = not self.ingame;

	def set_level(self, gamemap):
		if self.ingame == True:
			self.gamemap = Gamemap(gamemap)
			self.player = Player
			self.objects = Object_Set(self.gamemap)
			self.debug = False

	def open_menu(self):
		self.menuopen = True
		if (self.ingame):
			#Set up main menu:
			self.menu = Main_Menu
			print("Open Menu -- ingame")
		else:
			self.menu = Ingame_Menu
			print("Open Menu -- Out of game")

	def deal_menu(self):
		#if condtioions are right, close menu.
		#Determine how
		return RETURN

	def update(self):
		self._inputs.update()
		#what to do in the game:
		if (self.ingame):
			if self._inputs.ispressed("MENU"):
				self.open_menu()
			if (self.deal_menu == EXIT):
				self.menuopen = False

			#Update player:
			self.player.update(self._inputs, self.gamemap, self.objects)
			#Update map:
			self.objects.update(self.player, self.gamemap)
			#Update drawing
			self.draw_ingame()

		else:
			self.draw_outgame()

	def draw_outgame(self):
		self.mainmenu
