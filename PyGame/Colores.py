import pygame,sys
from pygame.locals import *

Color = (0,140,60)
Color2 = pygame.Color(255,120,9)
#simpre
pygame.init()
#creacion de ventana (objeto superficie)
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola mundo")

while True:
    ventana.fill(Color2)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()