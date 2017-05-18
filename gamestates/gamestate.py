#gamestate.h
import sys
import os

sys.path.append(os.path.abspath("../inputs"))
from keyboard_mouse import *

sys.path.append(os.path.abspath("../player"))
from player import *

sys.path.append(os.path.abspath("../map"))
from gamemap import *
from platform import *
GameMap()

sys.path.append(os.path.abspath("../objects"))
from object_set import *

sys.path.append(os.path.abspath("../menu"))
from menus import *

sys.path.append(os.path.abspath("../draw"))
from drawutils import *

EXIT = 0
RETURN = 1
KEEPOPEN = 3

def React_Phys(player, objects, gamemap):
	player.move()
	gamemap.hitbox(player)
	#objects.hitbox(player)
	#beams.move(player, gamemap, object)

class Gamestate:
	def __init__(self, inputs):
		self._inputs = inputs;
		self.ingame = False
		self.menuopen = True
		self.open_menu()
		self.menu_just_closed = False
		self.just_left_game = False

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
		self.player = Player(self.gamemap.starting_coords)
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
			print("Open Menu -- in game")
		else:
			#Set up main menu:
			self.menu = Main_Menu()
			print("Open Menu -- out of game")
	
	def close_menu(self, screen, background):
		self.menuopen = False
		self.menu.close(screen, background)
		print ("Exiting menu")

	def menu_state(self):
		#if condtioions are right, close menu.
		#Determine how
		return self.menu.get_state()
		

		#Potential errors in update so WATCHOUT

	def update(self):
		self._inputs.update()
		#what to do in the game:
		if self.ingame:
			#print (self.menuopen)
			if self.menuopen == True:
				self.menu.update()
				if (self.menu_state() == "MAIN MENU"):
					self.change_state()
					self.just_left_game = True
					self.menuopen = True
					self.menu_just_closed = True
				elif (self.menu_state() == "RETURN"):
					self.menu_just_closed = True
					self.menuopen = False


			else:	
				#Update player:
				self.player.update_keys(self._inputs)
			if self._inputs.ispressed("MENU"):
				self.open_menu()

		else:
			self.menu.update()
			if (self.menu_state() == "START"):
				self.change_state()
				self.menuopen = False
				self.menu_just_closed = True
			elif self.menu_state() == "EXIT":
				self.menu_just_closed = False
			elif self.menu_state() == "NORMAL":
				#Do nothing
				return
		



	def draw(self, drawutils, screen, background):
		if self.ingame:
			self.draw_ingame(drawutils, screen, background)
		else:
			self.draw_outgame(drawutils, screen, background)

	def draw_ingame(self, drawutils, screen, background):
		if self.menu_just_closed == True:
			self.close_menu(screen, background)
			self.menu_just_closed = False
		if self.menuopen:
			self.menu.draw(drawutils, screen)
		else:
			self.react(drawutils, screen, background)
			
		return

	
	#Determine how things should move, then move them.
	def react(self, drawutils, screen, background):
		#TODO: Add Reactions.
		React_Phys(self.player, self.objects, self.gamemap)	

		self.player.draw(drawutils, screen, background)
		self.objects.draw(drawutils, screen)
		self.gamemap.draw(drawutils, screen)
		return

	def draw_outgame(self, drawutils, screen, background):
		if (self.just_left_game == True):
			self.just_left_game = False
			self.player.close(screen, background)
			self.gamemap.close(drawutils, screen, background)
	
		if self.menu_just_closed:
			self.close_menu(screen, background)
			self.open_menu()
			self.menu_just_closed = False
		self.menu.draw(drawutils, screen)

