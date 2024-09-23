import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 630), pygame.RESIZABLE)
pygame.display.set_caption('Sorting Visualizer')

background = pygame.image.load('background.jpg').convert()
screen.blit(background, (0, 0))

pygame.display.flip()

arr_size = 40
arr = [random.randint(10, 550) for _ in range(arr_size)]
line_width = (1200 - (arr_size - 1) * 5 - 5) // arr_size
print('Line width =', line_width, 'Pixels')

def draw_bars(arr):
    x = 2.5
    for element in arr:
        element = pygame.Rect(0, 0, line_width, element)
        element.bottomleft = (x, 550)
        pygame.draw.rect(screen, (0, 0, 255), element)
        x += line_width + 5
    # pygame.display.update()
    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        else:
            draw_bars(arr)
    pygame.display.flip()
pygame.quit()