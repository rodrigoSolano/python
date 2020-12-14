import pygame,sys
from pygame.locals import *

size_window = (600,400)

def brakeGame():
    pygame.init()
    ventana = pygame.display.set_mode(size_window)
    background = pygame.image.load("C:/Users/rodri/Documents/Python/pygame/breakGame/background.jpg")
    coor_x = 250
    coor_y = 380
    width = 100
    heigth = 15
    Plataform = pygame.draw.rect(ventana,(120,120,120),(coor_x,coor_y,width,heigth))
    speed = 20

    ball = pygame.image.load("C:/Users/rodri/Documents/Python/pygame/ball.png")
    ballrect = ball.get_rect()

    while True:
        
        ventana.fill((255,255,255))
        pygame.draw.rect(ventana,(120,120,120),(coor_x,coor_y,width,heigth))
        pygame.draw.circle(ventana,(120,120,120),(80,80),20)
        coor_x = pygame.mouse.get_pos()[0]
        
        if ballrect.left < 0 or ballrect.right > 600:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > 400:
            speed[1] = -speed[1]

        ventana.blit(ball,ballrect)
        ballrect = ballrect.move(speed)

        if coor_x > 500:
            coor_x = 500

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    coor_x -= speed
                    if coor_x < 100:
                        coor_x = 0

                elif event.key == K_RIGHT:
                    coor_x += speed
                    if coor_x > 500:
                        coor_x = 500


        pygame.display.update()


def main():
    brakeGame()

if __name__ == "__main__":
    main()