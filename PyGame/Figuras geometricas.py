import pygame,sys
from pygame.locals import *

pygame.init()
size_window = (400,300)
bcolor = (255,255,255)

ventana = pygame.display.set_mode(size_window)
pygame.display.set_caption("Figuras")

#figuras

while True:
    ventana.fill(bcolor)
    pygame.draw.circle(ventana,(0,0,0),(80,80),20)
    pygame.draw.rect(ventana,(0,0,0),(150,150,100,100))
    pygame.draw.polygon(ventana,(0,0,0),((100,150),(150,200),(200,100),(100,0)))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()
    pygame.display.update()