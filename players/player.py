#player .py
import pygame
import sys
import os

from drawutils import *

X_SPEED = 3
Y_JUMPSPEED = 10
Y_GRAVITY = -.5

L_HOLD = 0
R_HOLD = 1
DUCK_HOLD = 2
MAX_HOLD = 3
class Player:
	def __init__(self, coords):
		self.inair = False
		self.x = coords[0]
		self.y = coords[1]
		self.gravity = -Y_GRAVITY
		self.x_speed = X_SPEED
		self.jumpspeed = -Y_JUMPSPEED
		#TODO: ADD
		self.image = pygame.image.load("res/player.png")
		#horizontal and vertical velocities
		self.x_velocity = 0
		self.y_velocity = 0 #   +
							#  -|+ 
							#   -
		self.canshoot = True

		self.holds = [False] * MAX_HOLD

	def move_x(self, inputs, gamemap, objects):
		return
	def move_y(self, inputs, gamemap, objects):
		return

	def left(self):
		if not self.holds[L_HOLD]:
			self.x_velocity+= -X_SPEED
			self.holds[L_HOLD] = True
	def unleft(self):
		if self.holds[L_HOLD]:
			self.x_velocity+=X_SPEED
			self.holds[L_HOLD] = False

	def right(self):
		if not self.holds[R_HOLD]:	
			self.x_velocity+=X_SPEED
			self.holds[R_HOLD] = True

	def unright(self):
		if self.holds[R_HOLD]:
			self.x_velocity+= -X_SPEED
			self.holds[R_HOLD] = False

	
	def jump(self):
		self.inair = True
		self.y_velocity += self.jumpspeed
		print 'Velocity: {}'.format(self.y_velocity)
		return
	def duck(self):
		return
	def shoot(self):
		return
	def update_keys(self, inputs):
		#Assume inputs are up to date
		if not self.inair:
			if inputs.ispressed("JUMP"):
				self.jump()
			if inputs.ispressed("LEFT"):
				self.left()
			else:
				self.unleft()
			if inputs.ispressed("RIGHT"):
				self.right()
			else:
				self.unright()
		if inputs.ispressed("DUCK"):
			self.duck()
		else:
			self.duck()
		if self.canshoot:
			if inputs.ispressed("SHOOT"):
				self.shoot()

	#set inair to true when in air	
	def draw_move(self, drawutils, screen, background):
#		self.inair = False
		
		screen.blit(background, (self.x, self.y), self.image.get_rect())
		self.x += self.x_velocity
		self.y += self.y_velocity
	
		if self.inair:	
			self.y_velocity += self.gravity
		#TODO: OTHER gravity things above ^	


		screen.blit(self.image, (self.x, self.y))
		return


