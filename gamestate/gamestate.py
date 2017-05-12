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

	def update(self):
		self._inputs.update
