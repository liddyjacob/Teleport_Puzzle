#menus.py
#Contains both menu classes
import sys
import os

import pygame

#print sys.path
sys.path.append(os.path.abspath("../inputs"))
from keyboard_mouse import *

#sys.path.append(os.path.abspath("../drawutils"))
from drawutils import *



X_START = 50
Y_START = 50

X_DIFF  = 20
Y_DIFF  = 30


class MenuItem:
	def __init__(self, text):
		self.text = text;
		#Default h and l
		self.set_height()
		self.set_length()
		self.pressed = False
		self.hover = False
	 
	def set_height(self, pixel_height = 20):	
		self.height = pixel_height

	def set_length(self, pixel_length = 80):
		self.length = pixel_length

	#Top left corner
	def set_location(self, x, y):
		self.x = x
		self.y = y

	#Index number
	def dynamic_location(self, item_number, indent_number = 0):
		self.x = X_START + X_DIFF * indent_number
		self.y = Y_START + Y_DIFF * item_number

	#See if mouse is in range:
	def inrange(self, coords):
		if (self.x <= coords[0]) and (self.x + self.length >= coords[0]):
			if (self.y <= coords[1]) and (self.y + self.height >= coords[1]):
				return True
		return False

	def update(self, input_):
		mouse_pos = pygame.mouse.get_pos()
		
		if self.inrange(mouse_pos):
			if (input_.ispressed("SHOOT")):
				self.pressed = True
				self.hover = True
			else:
				self.pressed = False
				self.hover = True
		else:
			self.pressed = False
			self.hover = False

	def draw(self, drawUtils, screen):
		if self.get_state() == "PRESSED":
			boxcolor = pygame.Color(255,255,255,255)
		if self.get_state() == "HOVER":
			boxcolor = pygame.Color(255,100,50,10)
		if self.get_state() == "NORMAL":
			boxcolor = pygame.Color(15,50,100,10)

		pygame.draw.rect(screen, boxcolor, [self.x, self.y, self.length, self.height])

		screen.blit(drawUtils.font.render(self.text, True, (255,255,255)), (self.x, self.y))
		pygame.display.update()


	def get_state(self):
		if (self.pressed):
			return "PRESSED"
		if (self.hover):
			return "HOVER"
		return "NORMAL"

	def ispressed(self):
		if self.get_state() == "PRESSED":
			return True
		return False

	def close(self, screen, background):
		print 'Closing {}'.format(self.text)
		screen.blit(background, (self.x, self.y), pygame.Rect(self.x, self.y, self.length, self.height))
	

class Menu:
	def __init__(self, item_text,  controls = Keyboard_Mouse(), dynamic = True):
		self.input = controls
		#Tuples in form (TEXT, MENUITEM)
		self.item_list = []
		self.set_item_text(item_text)
		self.open = True
		
		if dynamic:
			self.dynamic_item_locations()

	def set_item_text(self, item_text):	
		for text in item_text:
			self.item_list.append(MenuItem(text))

	def dynamic_item_locations(self):
		index = 0
		for item in self.item_list:
			item.dynamic_location(index)
			index+=1
			

	def update(self):
		self.input.update
		for item in self.item_list:
			item.update(self.input)

	def get_state(self):
		for item in self.item_list:
			item.update(self.input)
			if item.ispressed():
				return item.text.upper()
		return "NORMAL"

	def draw(self, drawutils, screen):
		if self.open:
			self.input.update()
			for item in self.item_list:
				item.draw(drawutils, screen)			
		else:
			print("ERROR: Menu Closed!")

	def close(self, screen, background):
		self.open = False
		for item in self.item_list:
			item.close(screen, background)

#TODO: This is just a copy of Main_menu(): Fix
class Ingame_Menu(Menu):
	def __init__(self, control = Keyboard_Mouse()):		
		Menu.__init__(self,["RETURN", "MAIN MENU"], control)

class Main_Menu(Menu):
	def __init__(self, control = Keyboard_Mouse()):		
		Menu.__init__(self,["START", "LOAD" ,"SETTINGS","EXIT"], control)


