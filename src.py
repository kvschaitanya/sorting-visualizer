import pygame

pygame.init()

screen = pygame.display.set_mode((1300, 700), pygame.RESIZABLE)
background = pygame.image.load('background.jpg').convert()
screen.blit(background, (0, 0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        else:
            pass
    pygame.display.flip()
pygame.quit()