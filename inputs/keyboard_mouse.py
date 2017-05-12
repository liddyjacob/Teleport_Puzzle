import pygame

JUMP = 0
DUCK = 1
LEFT = 2
RIGHT = 3
SHOOT = 4


class Keyboard_Mouse:
	def __init__(self):
		self.jump_key  = pygame.K_SPACE
		self.duck_key  = pygame.K_s
		self.left_key  = pygame.K_a
		self.right_key = pygame.K_d
		self.mouse     = True
		self.mouse_but = 1
		self.shoot     = pygame.MOUSEBUTTONDOWN

		self.tapped = [(0, False), (1, False), (2, False), (3, False), (4, False)]
		self.pressed = [(0, False), (1, False), (2, False), (3, False), (4, False)]


	def getKeyNo(self, string):
		if (string == "JUMP"):
			return JUMP
		if (string == "DUCK"):
			return DUCK
		if (string == "LEFT"):
			return LEFT
		if (string == "RIGHT"):
			return RIGHT
		if (string == "SHOOT"):
			return SHOOT
		print("Error in _getKeyNo: Invalid Key.")
		return -1

	def set_jump(self, key):
		self.jump_key = key

	def set_duck(self, key):
		self.duck_key = key

	def set_left(self, key):
		self.left_key = key

	def set_right(self, key):
		self.right_key = key

	#is the key tapped?
	def tapped(self, key_str):
		key_int = self.getKeyNo(key_str)
		#Handle bad string:
		if (key_int == -1):
			return
		return tapped[key_str][1];

	def pressed(self, key_str):
		key_int = self.getKeyNo(key_str)
		#Handle bad string:
		if (key_int == -1):
			return
		return pressed[key_str][1];

	#Update the keyboard:
	def update():
		return	
