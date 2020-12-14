import pygame,sys
from pygame.locals import *

pygame.init()
size_window = (600,500)
bcolor = (255,255,255)

ventana = pygame.display.set_mode(size_window)
pygame.display.set_caption("Load y blit")

image = pygame.image.load("C:/Users/rodri/Documents/Python/pygame/ball.png")

while True:
    ventana.fill(bcolor)
    ventana.blit(image,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()