#drawutils.py
#To help draw everything!
import pygame

class Drawutils:
	def __init__(self, screen):
		self.font = pygame.font.SysFont("Monospace", 14);
		self.screen_w = 700 
		self.screen_h = 500
		self.screen = screen

	def drawStringCenter(self, color, x, y, string, bold):
		self.drawStringHelper(color, x, y, string, bold)


	def drawStringHelper(self, color, x, y, string, bold):
		# render text
		label = self.font.render("Some text!", 1, (255,255,0))
		screen.blit(label, (x, y))

	def drawBox(self, screen, boxcolor, location, length, height):
		pygame.draw.rect(screen, boxcolor, [location[0], location[1], length, height]) 
		pygame.display.update()

	def closeBox(self, screen, background, location, length, height):
		screen.blit(background, location, pygame.Rect(location[0], location[1], length, height))
	

