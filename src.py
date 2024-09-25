import pygame
import random

pygame.init()
pygame.font.init()

calibri18 = pygame.font.SysFont('calibri', 18, True)
calibri18.set_underline(True)
calibri16 = pygame.font.SysFont('calibri', 16, True)
impact = pygame.font.SysFont('impact', 30)

BACKGROUND = [37, 37, 37]
BAR = [0, 143, 148]
HIGHLIGHTED_BAR = [105, 48, 195]
COMPLETED_BAR = [57, 255, 20]

arr_size = 40 # default, 100 = huge, 80 = big, 40 = medium, 20 = small, 10 = very small
delay_time = 20 # 0 = instant, 10 = fast, 20 = normal, 30 = slow, 40 = very slow
# 0 = Bubble Sort, 1 = Selection Sort, 2 = Quick Sort, 3 = Merge Sort, 4 = Heap Sort
color_index = [BAR for _ in range(arr_size)]
line_width = (1200 - (arr_size - 1) * 5 - 5) // arr_size
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

start_rect = pygame.Rect(620, 550, 180, 60)
refresh_rect = pygame.Rect(900, 550, 200, 60)

screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Sorting Algorithm Visualizer')
screen.fill(BACKGROUND)
pygame.display.flip()

arr = [random.randint(10, 500) for _ in range(arr_size)]

def draw_bars(arr:list):
    screen.fill(BACKGROUND, (0, 0, 1200, 500))
    x = 2
    for index, element in enumerate(arr):
        element = pygame.Rect(0, 0, line_width, element)
        element.bottomleft = (x, 500)
        pygame.draw.rect(screen, color_index[index], element, border_top_left_radius = 3,border_top_right_radius = 3)
        x += line_width + 5
    pygame.display.update((0, 0, 1200, 500))

def draw_circles():
    for index in range(3):
        for pos in circle_pos[index]:
            pygame.draw.circle(screen, (192, 192, 192), pos, 7)
    
    pygame.draw.circle(screen, (20, 20, 20), circle_pos[0][2], 4)
    pygame.draw.circle(screen, (20, 20, 20), circle_pos[1][2], 4)
    pygame.draw.circle(screen, (20, 20, 20), circle_pos[2][0], 4)

    screen.blit(calibri18.render("Array Size:", True, (240, 240, 240)), (5, 505))
    screen.blit(calibri18.render("Speed:", True, (240, 240, 240)), (185, 505))
    screen.blit(calibri18.render("Algorithm:", True, (240, 240, 240)), (365, 505))

    screen.blit(calibri16.render("Huge", True, (240, 240, 240)), (35, 532))
    screen.blit(calibri16.render("Big", True, (240, 240, 240)), (35, 557))
    screen.blit(calibri16.render("Medium", True, (240, 240, 240)), (35, 582))
    screen.blit(calibri16.render("Small", True, (240, 240, 240)), (35, 607))
    screen.blit(calibri16.render("Very Small", True, (240, 240, 240)), (35, 632))

    screen.blit(calibri16.render("Very Quick", True, (240, 240, 240)), (215, 532))
    screen.blit(calibri16.render("Fast", True, (240, 240, 240)), (215, 557))
    screen.blit(calibri16.render("Normal", True, (240, 240, 240)), (215, 582))
    screen.blit(calibri16.render("Slow", True, (240, 240, 240)), (215, 607))
    screen.blit(calibri16.render("Very Slow", True, (240, 240, 240)), (215, 632))

    screen.blit(calibri16.render("Bubble Sort", True, (240, 240, 240)), (395, 532))
    screen.blit(calibri16.render("Selection Sort", True, (240, 240, 240)), (395, 557))
    screen.blit(calibri16.render("Quick Sort", True, (240, 240, 240)), (395, 582))
    screen.blit(calibri16.render("Merge Sort", True, (240, 240, 240)), (395, 607))
    screen.blit(calibri16.render("Heap Sort", True, (240, 240, 240)), (395, 632))

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
                        refresh()

                    elif index == 1:
                        pygame.draw.circle(screen, (192, 192, 192), circle_pos[1][circle_val[1].index(delay_time)], 7)
                        delay_time = circle_val[index][i]
                        pygame.draw.circle(screen, (20, 20, 20), pos, 4)
                    # else:
                    #     pass
    pygame.display.update()

def draw_buttons(mouse_pos = (0, 0)):
    if start_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (226, 62, 87), start_rect, border_radius = 4)
    else:
        pygame.draw.rect(screen, (170, 48, 78), start_rect, border_radius = 4)
    screen.blit(impact.render("Start", True, (200, 200, 200)), (680, 560))
    screen.blit(calibri16.render("or press s", False, (200, 200, 200)), (670, 615))

    if refresh_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (100, 190, 80), refresh_rect, border_radius = 4)
    else:
        pygame.draw.rect(screen, (95, 141, 78), refresh_rect, border_radius = 4)
    screen.blit(impact.render("Refresh", True, (200, 200, 200)), (950, 560))
    screen.blit(calibri16.render("or press r", False, (200, 200, 200)), (940, 615))

    pygame.display.update([(620, 550, 180, 110), (900, 550, 200, 110)])

def push_buttons(mouse_pos):
    if start_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (150, 30, 50), start_rect, border_radius = 4)
        screen.blit(impact.render("Start", True, (200, 200, 200)), (680, 560))
        pygame.display.update(start_rect)
        bubblesort(arr)
    elif refresh_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (70, 120, 50), refresh_rect, border_radius = 4)
        screen.blit(impact.render("Refresh", True, (200, 200, 200)), (950, 560))
        pygame.display.update(refresh_rect)
        refresh()

def refresh():
    global color_index, arr, line_width
    arr = [random.randint(10, 500) for _ in range(arr_size)]
    line_width = (1200 - (arr_size - 1) * 5 - 5) // arr_size
    color_index = [BAR for _ in range(arr_size)]
    draw_bars(arr)

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
draw_buttons()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            draw_buttons(event.dict.get('pos'))
        elif event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_s:
                bubblesort(arr)
            elif event.dict['key'] == pygame.K_r:
                refresh()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            push_buttons(event.dict['pos'])
            mark_circle(event.dict['pos'])
pygame.quit()