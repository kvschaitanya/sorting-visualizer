import pygame
import random

pygame.init()
pygame.font.init()

calibri18 = pygame.font.SysFont('calibri', 18, True)
calibri18.set_underline(True)
calibri16 = pygame.font.SysFont('calibri', 16, True)
impact = pygame.font.SysFont('impact', 30)

BACKGROUND = [37, 37, 37]
BAR = [0, 133, 138]
HIGHLIGHTED_BAR = [105, 48, 195]
COMPLETED_BAR = [57, 255, 20]
WORKING_PORTION = [100, 223, 228]

arr_size = 40 # default, 100 = huge, 80 = big, 40 = medium, 20 = small, 10 = very small
delay_time = 20 # 0 = instant, 10 = fast, 20 = normal, 30 = slow, 40 = very slow
algorithm = 0 # 0 = Bubble Sort, 1 = Selection Sort, 2 = Quick Sort, 3 = Merge Sort, 4 = Heap Sort

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
    screen.blit(calibri16.render("Merge Sort", True, (240, 240, 240)), (395, 557))
    screen.blit(calibri16.render("Quick Sort", True, (240, 240, 240)), (395, 582))
    screen.blit(calibri16.render("Selection Sort", True, (240, 240, 240)), (395, 607))
    screen.blit(calibri16.render("Heap Sort", True, (240, 240, 240)), (395, 632))

    pygame.display.update()

def mark_circle(marked_pos):
    global arr_size, delay_time, algorithm
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
                    elif index == 2:
                        pygame.draw.circle(screen, (192, 192, 192), circle_pos[2][circle_val[2].index(algorithm)], 7)
                        algorithm = circle_val[index][i]
                        pygame.draw.circle(screen, (20, 20, 20), pos, 4)
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
        sort()
    elif refresh_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (70, 120, 50), refresh_rect, border_radius = 4)
        screen.blit(impact.render("Refresh", True, (200, 200, 200)), (950, 560))
        pygame.display.update(refresh_rect)
        refresh()

def refresh():
    global color_index, arr, line_width, arr_size
    arr = [random.randint(10, 500) for _ in range(arr_size)]
    line_width = (1200 - (arr_size - 1) * 5 - 5) // arr_size
    color_index = [BAR for _ in range(arr_size)]
    draw_bars(arr)

def sort():
    if algorithm == 0:
        bubblesort(arr)
    elif algorithm == 1:
        mergesort(arr, 0, arr_size - 1)
    elif algorithm == 2:
        quicksort(arr, 0, arr_size - 1)
    elif algorithm == 3:
        selectionsort(arr)
    else:
        pass
    draw_bars(arr)

def bubblesort(arr:list):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            color_index[j] = HIGHLIGHTED_BAR
            color_index[j + 1] = HIGHLIGHTED_BAR
            
            pygame.event.pump()
            draw_bars(arr)

            pygame.time.delay(delay_time)

            color_index[j] = BAR
            color_index[j + 1] = BAR
        color_index[i] = COMPLETED_BAR
        pygame.event.pump()
        draw_bars(arr)

def mergesort(arr : list, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    mergesort(arr, left, mid)
    mergesort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge(arr : list, l, m, r):
    for i in range(l, r + 1):
        color_index[i] = WORKING_PORTION
    draw_bars(arr)
    pygame.event.pump()

    l_temp = arr[l : m + 1]
    r_temp = arr[m + 1 : r + 1]

    i = j = 0
    k = l
    while(i < len(l_temp) and j < len(r_temp)):
        if l_temp[i] <= r_temp[j]:
            arr[k] = l_temp[i]
            i += 1
            k += 1
        else:
            arr[k] = r_temp[j]
            j += 1
            k += 1
        color_index[k - 1] = COMPLETED_BAR
        pygame.time.delay(delay_time)
        draw_bars(arr)
        pygame.event.pump()

    while(i < len(l_temp)):
        arr[k] = l_temp[i]
        i += 1
        k += 1
        color_index[k - 1] = COMPLETED_BAR
        pygame.time.delay(delay_time)
        draw_bars(arr)
        pygame.event.pump()
    while(j < len(r_temp)):
        arr[k] = r_temp[j]
        j += 1
        k += 1
        color_index[k - 1] = COMPLETED_BAR
        pygame.time.delay(delay_time)
        draw_bars(arr)
        pygame.event.pump()

def quicksort(arr : list, left, right):
    if left >= right:
        if left == right:
            color_index[left] = COMPLETED_BAR
        return
        
    for i in range(left, right):
        color_index[i] = WORKING_PORTION

    pivot = arr[right]
    color_index[right] = HIGHLIGHTED_BAR
    draw_bars(arr)
    pygame.event.pump()

    i = left
    for j in range(left, right):
        color_index[j] = HIGHLIGHTED_BAR
        draw_bars(arr)
        pygame.event.pump()
        pygame.time.delay(delay_time)
        color_index[j] = WORKING_PORTION
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            color_index[i] = COMPLETED_BAR
            draw_bars(arr)
            pygame.event.pump()
            pygame.time.delay(delay_time)
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    color_index[i] = COMPLETED_BAR

    for t in range(i + 1, right + 1):
        color_index[t] = BAR
    draw_bars(arr)
    pygame.event.pump()
    quicksort(arr, left, i - 1)
    quicksort(arr, i + 1, right)

def selectionsort(arr : list):
    for i in range(arr_size):
        index_minimum = i
        color_index[index_minimum] = HIGHLIGHTED_BAR
        for j in range(i + 1, arr_size):
            color_index[j] = HIGHLIGHTED_BAR
            pygame.time.delay(delay_time)
            draw_bars(arr)
            pygame.event.pump()
            color_index[j] = BAR

            if arr[j] < arr[index_minimum]:
                color_index[index_minimum] = BAR

                index_minimum = j

                color_index[index_minimum] = HIGHLIGHTED_BAR
                pygame.time.delay(delay_time)
                draw_bars(arr)
                pygame.event.pump()

        arr[i], arr[index_minimum] = arr[index_minimum], arr[i]
        color_index[index_minimum] = BAR
        color_index[i] = COMPLETED_BAR
        draw_bars(arr)
        pygame.event.pump()

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
                sort()
            elif event.dict['key'] == pygame.K_r:
                refresh()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            push_buttons(event.dict['pos'])
            mark_circle(event.dict['pos'])
pygame.quit()