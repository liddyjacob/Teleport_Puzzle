#This function should load the gamemap and its objects independantly,
#based off a specialized file
import pygame 
import os
import sys 

class Platform:
    def __init__(self, location, length, height, image_file):
		self.location = location
		self.length = length
		self.height = height
        #TODO: ADD REAL TEXTURE FILES AND REMOVE THIS:
		image_file = pygame.Color(15,70,90,20)
		self.texture = image_file
        #self.texture = pygame.image.load(image_file)

    #See if the platform is stopping the player:
    def hitboxed(self, player_pos):
        return

    def draw(self, drawutils, screen):
        drawutils.drawBox(screen, self.texture, self.location, self.length, self.height)

    def close(self, drawutils, screen, background):
		drawutils.closeBox(screen, background, self.location, self.length, self.height)
		return

#A thin platform without a bottom
class Traverse_Platform(Platform):
    def __init__(self, location, length):
        texture_file = "res/thinwall.png"
        Platform.__init__(self, location, length, 5, texture_file)

    def hitboxed(self, player):
        print "In traverse hitboxed"
        return


class Solid_Platform(Platform):
	def __init__(self, location, length, height, texture_file = "res/thickwall"):
		Platform.__init__(self, location, length, height, texture_file)
		self.a = 'a'
		#FIXME? Watch for clipping errors here

	def inrange_x(self, player_x, player_length):
		return not set(range(player_x, player_x + player_length)).isdisjoint(range(self.location[0], self.location[0] + self.length))
	
	def inrange_y(self, player_y, player_height):
		player_set = set(range(int(player_y), int(player_y) + player_height))
		platform_set = set(range(self.location[1], self.location[1] + self.height))
		return not player_set.isdisjoint(platform_set)
	def inrange(self, player):
		if self.inrange_x(player.x, player.length):
			if self.inrange_y(player.y, player.height):
				return True	
		return False

	def modify_player(self, player):
		#Player's old Y was out of bounds-
		if (self.inrange_y(player.old_y, player.height)):
			player.y = self.location[1] - player.height - 45
			player.inair = False		 

	def hitboxed(self, player):

		if self.inrange(player):
			print "Inrange"
			self.modify_player(player)
			pygame.event.post(pygame.event.Event(pygame.USEREVENT, message = "Hitboxed!"))
				#Check which can be undone- y first
				#if self.inrange(player.y - player.y_velocity, player.height):
				#	player.y_velocity = 0
					#Above platform?
				#	if player.y - player.height - player.y_velocity < self.location[1]:
				#		player.inair = False
				#		player.y = self.location[1] - player.height
		else:
			print "Out of range"
					
		
		
		print "In solid hitbox"
		return




def Load_Gamemap(str_gamemap, gamemap, objects):
	return

class GameMap:
	def __init__(self):
		self.test = "test"

	#def 

#Basic hardcoded gamemap for testing purposes:
class Basic_Gamemap(GameMap):
	def __init__(self):
		self.starting_coords = (100, 100)
		print("Basic_Gamemap Loading...")

		self.platforms = [Solid_Platform((50,350), 100 , 20 ,"res/pencil.png"),Solid_Platform((50,50), 100, 20, "res/pencil.png")]		

	def initial_objects():
		print "a"

	def hitbox(self, player):
		for platform in self.platforms:
			platform.hitboxed(player)
		return


	def draw(self, drawutils, screen):
		for platform in self.platforms:
			platform.draw(drawutils, screen)
		return

	def close(self, drawutils, screen, background):
		for platform in self.platforms:
			platform.close(drawutils, screen, background)
		return

	
