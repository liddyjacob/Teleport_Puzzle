import pygame

JUMP = 0
DUCK = 1
LEFT = 2
RIGHT = 3
SHOOT = 4
MENU = 5

MAXKEY = 6

class Keyboard_Mouse:
	def __init__(self):
		self.key = [pygame.K_SPACE, pygame.K_s, pygame.K_a, pygame.K_d, pygame.MOUSEBUTTONDOWN, pygame.K_ESC]
		self.key[JUMP]  = pygame.K_SPACE
		self.key[DUCK] = pygame.K_s
		self.key[LEFT]  = pygame.K_a
		self.key[RIGHT] = pygame.K_d
		self.mouse     = True
		self.mouse_but = 1
		self.key[SHOOT]     = pygame.MOUSEBUTTONDOWN

		self.tapped = [False] * MAXKEY
		self.pressed = [False] * MAXKEY


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
		if (string )
		print("Error in _getKeyNo: Invalid Key.")
		return -1

	def set_jump(self, key):
		self.key[JUMP] = key

	def set_duck(self, key):
		self.key[DUCK] = key

	def set_left(self, key):
		self.key[LEFT] = key

	def set_right(self, key):
		self.key[RIGHT] = key

	#is the key tapped?
	def istapped(self, key_str):
		key_int = self.getKeyNo(key_str)
		#Handle bad string:
		if (key_int == -1):
			return
		return self.tapped[key_int];

	def ispressed(self, key_str):
		key_int = self.getKeyNo(key_str)
		#Handle bad string:
		if (key_int == -1):
			return
		return self.pressed[key_int];

	#Update the keyboard:
	def update(self):
		#Get all keys pressed:
		keys=pygame.key.get_pressed()

		for index in range(JUMP, SHOOT + 1):
			#If the key was not pressed:
			if (self.pressed[index] == False):
				#Press if pressed:
				self.pressed[index] = keys[self.key[index]]
				self.tapped[index] = keys[self.key[index]]
			else:
				#Obviously if it was already pressed it was not tapped: 
				self.tapped[index] = False;
				self.pressed[index] = keys[self.key[index]];
		return
