FPS = 60

#Main.py
#Python - Main game
import sys
import os

import pygame
from pygame.locals import *

sys.path.append(os.path.abspath("draw/"))

#hi = Drawutils()
sys.path.append(os.path.abspath("players/"))
sys.path.append(os.path.abspath("map/"))
sys.path.append(os.path.abspath("inputs/"))
sys.path.append(os.path.abspath("menu/"))
sys.path.append(os.path.abspath("objects/"))
from player import *
from drawutils import Drawutils
from menus import *
from keyboard_mouse import *
from object_set import *
from platform import *

from gamemap import *
sys.path.append(os.path.abspath("gamestates/"))
from gamestate import *
#Platform()

def main():

	pygame.init()
	screen = pygame.display.set_mode((700, 500))
	pygame.display.set_caption('Basic Pygame program')
	background = pygame.Surface(screen.get_size())

	fps = FPS
	fpsClock = pygame.time.Clock()

	inputs = Keyboard_Mouse()
	drawutils = Drawutils(screen)
	menu = Main_Menu()
	gamestate = Gamestate(inputs)
	pygame.display.flip()

	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			else:
				gamestate.update()
				
				if gamestate.menuopen == True:
					state = gamestate.menu_state()
					if state == "EXIT":
						return
					if state == "START":
						print("Start")
		gamestate.draw(drawutils, screen, background)
		#if menu.get_state() == "START"
#        screen.blit(background, (0, 0))
		pygame.display.flip()
		fpsClock.tick(fps)


if __name__ == '__main__': main()

#print "hi"

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
