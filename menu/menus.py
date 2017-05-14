#menus.py
#Contains both menu classes

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


	def update(self, input_):
		mouse_pos = pygame.mouse.get_rel()
		if 
		input_.ispressed



class Main_Menu:
	#Set up a main menu:
	def __init__(self):
		self.menu
