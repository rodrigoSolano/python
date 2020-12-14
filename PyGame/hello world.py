import pygame,sys
from pygame.locals import *

#simpre
pygame.init()
#creacion de ventana (objeto superficie)
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola mundo")

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()