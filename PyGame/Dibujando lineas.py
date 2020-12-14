import pygame,sys
from pygame.locals import *

Color = (0,140,60)
Color2 = (0,0,0)
#simpre
pygame.init()
#creacion de ventana (objeto superficie)
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola mundo")

pygame.draw.line(ventana,Color2,(0,0),(200,200),100)

while True:
    ventana.fill(Color)
    pygame.draw.line(ventana,Color2,(0,0),(200,200),10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()