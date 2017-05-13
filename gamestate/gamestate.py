#gamestate.h
import sys
import os
sys.path.append(os.path.abspath("../inputs"))
from keyboard_mouse import *

class Gamestate:
	def __init__(self, inputs):
		self._inputs = inputs;
		self.ingame = False


	def change_state(self):
		self.ingame = not self.ingame;
		if self.ingame == True:
			self.player = Player
			self.gamemap = Gamemap
			self.objects = []
			self.debug = False

	def update(self):
		self._inputs.update()
		if _inputs.mouse
