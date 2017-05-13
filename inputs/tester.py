from keyboard_mouse import *
import pygame
test = Keyboard_Mouse()

print(test.ispressed("JUMP"))

pygame.init()
screen = pygame.display.set_mode((150, 50))

change = False
lastkey = False
while (1):

	#Clear event queue:	
	for event in pygame.event.get():
		if (event.type == pygame.KEYDOWN) or event.type == pygame.KEYUP:
			test.update()
			for i in ["JUMP", "DUCK", "LEFT", "RIGHT", "SHOOT"]:
				test.update()
				print (test.ispressed(i))
		if event.type == pygame.QUIT:
			exit()

	keys = pygame.key.get_pressed()

	if (lastkey != keys[pygame.K_w]):
		print("W touched!")

	lastkey = keys[pygame.K_w]	
	pygame.event.pump()
	test.update()

	
