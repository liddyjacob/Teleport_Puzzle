#menus.py
#Contains both menu classes
import sys
import os

sys.path.append(os.path.abspath("../inputs"))
from keyboard_mouse import *

import pygame

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

	 
	def set_height(self, pixel_height = 20):	
		self.height = pixel_heigth

	def set_length(self, pixel_length = 70):
		self.length = pixel_length

	#Top left corner
	def set_location(self, x, y):
		self.x = x
		self.y = y

	#Index number
	def dynamic_location(self, item_number, indent_number = 0):
		self.x = X_START + X_DIFF * indend_number
		self.Y = Y_START + Y_DIFF * item_number

	#See if mouse is in range:
	def inrange(self, coords):
		if (self.x <= coords[0]) and (self.x + self.length >= coords[0]):
			if (self.y <= coords[1]) and (self.y + self.heigth >= coords[1]):
				return True
		return False

	def update(self, input_):
		mouse_pos = pygame.mouse.get_rel()
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

	def get_state(self):
		if (self.pressed):
			return "PRESSED"
		if (self.hover):
			return "HOVER"
		return "NORMAL"


class Main_Menu:
	#Set up a main menu:
	def __init__(self):
		self.start = MenuItem("START")
		self.exit = MenuItem("EXIT")

		self.start.dynamic_location(0)
		self.exit.dynamic_location(1)

	def update(self):
		self.start.update()
		self.exit.update()

	def get_state(self):
		if start.get_state() == "PRESSED":
			return "START"
		if exit.get_state() == "PRESSED":
			return "EXIT"
		#Else
		return "NORMAL"

	
			
