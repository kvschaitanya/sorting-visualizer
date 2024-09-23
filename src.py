import pygame
import random

pygame.init()

BACKGROUND = (37, 37, 37)
BAR = (0, 143, 148)
HIGHLIGHTED_BAR = (105, 48, 195)
COMPLETED_BAR = (57, 255, 20)

screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Sorting Algorithm Visualizer')

screen.fill(BACKGROUND)
pygame.display.flip()

arr_size = 40
arr = [random.randint(10, 500) for _ in range(arr_size)]
line_width = (1200 - (arr_size - 1) * 5 - 5) // arr_size
print('Line width =', line_width, 'Pixels')
color_index = [BAR for _ in range(arr_size)]

def draw_bars(arr):
    screen.fill(BACKGROUND)
    x = 2.5
    for index, element in enumerate(arr):
        element = pygame.Rect(0, 0, line_width, element)
        element.bottomleft = (x, 500)
        pygame.draw.rect(screen, color_index[index], element)
        x += line_width + 5
    pygame.display.update()
    
def bubblesort(arr):
    draw_bars(arr)
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            color_index[j] = HIGHLIGHTED_BAR
            color_index[j + 1] = HIGHLIGHTED_BAR
            draw_bars(arr)

            pygame.time.delay(10)

            color_index[j] = BAR
            color_index[j + 1] = BAR
        color_index[i] = COMPLETED_BAR

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        elif event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_s:         # Event(768-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})
            bubblesort(arr)

    screen.fill(BACKGROUND)   
    pygame.display.flip()
pygame.quit()