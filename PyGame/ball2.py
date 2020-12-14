import sys,pygame

pygame.init()

size = 800,600
screen = pygame.display.set_mode(size)

pygame.display.set_caption("juego baall")

width,height = 800,600
speed = [1,1]
white = 120,120,120

ball = pygame.image.load("C:/Users/rodri/Documents/Python/pygame/ball.png")
ballrect = ball.get_rect()

run = True

while run:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    screen.fill(white)
    screen.blit(ball,ballrect)
    pygame.display.flip()

pygame.quit()