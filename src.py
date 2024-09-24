import pygame
import random

pygame.init()

BACKGROUND = (37, 37, 37)
BAR = (0, 143, 148)
HIGHLIGHTED_BAR = (105, 48, 195)
COMPLETED_BAR = (57, 255, 20)

arr_size = 40 # default, 100 = huge, 80 = big, 40 = medium, 20 = small, 10 = very small
delay_time = 20 # 0 = instant, 10 = fast, 20 = normal, 30 = slow, 40 = very slow
# 0 = Bubble Sort, 1 = Selection Sort, 2 = Quick Sort, 3 = Merge Sort, 4 = Heap Sort
color_index = [BAR for _ in range(arr_size)]
circle_pos = (((20, 540),
          (20, 565), 
          (20, 590), 
          (20, 615), 
          (20, 640)),

         ((200, 540),
          (200, 565),
          (200, 590),
          (200, 615),
          (200, 640)),

         ((380, 540), 
          (380, 565), 
          (380, 590), 
          (380, 615),
          (380, 640)))

circle_val = ((100, 80, 40, 20, 10), 
              (0, 10, 20, 30, 40), 
              (0, 1, 2, 3, 4))

screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Sorting Algorithm Visualizer')
screen.fill(BACKGROUND)
pygame.display.flip()

arr = [random.randint(10, 500) for _ in range(arr_size)]
line_width = (1200 - (arr_size - 1) * 5 - 5) // arr_size
print('Line width =', line_width, 'Pixels')

def draw_bars(arr:list):
    screen.fill(BACKGROUND, (0, 0, 1200, 500))
    x = 2
    for index, element in enumerate(arr):
        element = pygame.Rect(0, 0, line_width, element)
        element.bottomleft = (x, 500)
        pygame.draw.rect(screen, color_index[index], element)
        x += line_width + 5
    pygame.display.update((0, 0, 1200, 500))

def draw_circles():
    for index in range(3):
        for pos in circle_pos[index]:
            pygame.draw.circle(screen, (192, 192, 192), pos, 7)
    
    pygame.draw.circle(screen, (20, 20, 20), circle_pos[0][2], 4)
    pygame.draw.circle(screen, (20, 20, 20), circle_pos[1][2], 4)
    pygame.draw.circle(screen, (20, 20, 20), circle_pos[2][2], 4)

    pygame.display.update()

def mark_circle(marked_pos):
    global arr_size, delay_time
    if marked_pos:
        for index in range(3):
            for i, pos in enumerate(circle_pos[index]):
                if ((pos[0] - marked_pos[0]) ** 2 + (pos[1] - marked_pos[1]) ** 2) ** 0.5 <= 7:
                    if index == 0:
                        pygame.draw.circle(screen, (192, 192, 192), circle_pos[0][circle_val[0].index(arr_size)], 7)
                        arr_size = circle_val[index][i]
                        pygame.draw.circle(screen, (20, 20, 20), pos, 4)

                    elif index == 1:
                        pygame.draw.circle(screen, (192, 192, 192), circle_pos[1][circle_val[1].index(delay_time)], 7)
                        delay_time = circle_val[index][i]
                        pygame.draw.circle(screen, (20, 20, 20), pos, 4)
                    # else:
                    #     pass
    pygame.display.update()

def bubblesort(arr:list):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            color_index[j] = HIGHLIGHTED_BAR
            color_index[j + 1] = HIGHLIGHTED_BAR
            draw_bars(arr)

            pygame.time.delay(delay_time)

            color_index[j] = BAR
            color_index[j + 1] = BAR
        color_index[i] = COMPLETED_BAR
        draw_bars(arr)

draw_bars(arr)
draw_circles()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        elif event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_s:         # Event(768-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})
            bubblesort(arr)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if option:
            #     pass
            mark_circle(event.dict['pos'])
            print(arr_size, delay_time)
pygame.quit()