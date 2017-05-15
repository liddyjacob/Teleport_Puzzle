#drawutils.py
#To help draw everything!
import pygame

class Drawutils:
	def __init__(self):
		self.font = pygame.font.SysFont("Monospace", 14);
		self.screen_w = 700 
		self.screen_h = 500

	def drawStringCenter(self, color, x, y, string, bold):
		self.drawStringHelper(color, x, y, string, bold)


	def drawStringHelper(self, color, x, y, string, bold):
		# render text
		label = self.font.render("Some text!", 1, (255,255,0))
		screen.blit(label, (x, y))	
