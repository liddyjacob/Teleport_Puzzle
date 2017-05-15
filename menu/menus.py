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

	 
	def set_height(self, pixel_height = 20):	
		self.height = pixel_height

	def set_length(self, pixel_length = 70):
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
		print mouse_pos
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


class Main_Menu:
	#Set up a main menu:
	def __init__(self):
		self.input = Keyboard_Mouse()
		self.start = MenuItem("START")
		self.exit = MenuItem("EXIT")

		self.start.dynamic_location(0)
		self.exit.dynamic_location(1)

	def update(self):
		self.input.update()
		self.start.update(self.input)
		self.exit.update(self.input)

	def get_state(self):
		if self.start.get_state() == "PRESSED":
			return "START"
		if self.exit.get_state() == "PRESSED":
			return "EXIT"
		#Else
		return "NORMAL"


	def draw(self, drawutils, screen):
		self.input.update()
		self.start.draw(drawutils, screen)
		self.exit.draw(drawutils, screen)	
			
