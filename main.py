#Main.py
#Python - Main game
import sys
import os

import pygame
from pygame.locals import *


sys.path.append(os.path.abspath("menu/"))
sys.path.append(os.path.abspath("inputs/"))
from menus import *




def main():

	pygame.init()
	screen = pygame.display.set_mode((700, 500))
	pygame.display.set_caption('Basic Pygame program')

	menu = Main_Menu()
	pygame.display.flip()

	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			else:
				menu.update()

#        screen.blit(background, (0, 0))
		pygame.display.flip()


if __name__ == '__main__': main()

print "hi"

"""
def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()
"""
