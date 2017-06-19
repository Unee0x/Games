import pygame
from math import *
import time

win = pygame.display.set_mode((400, 600))

running = True

t = pygame.time.Clock()
fps = 1


def draw_circle():
    circle_surface = pygame.Surface((100, 100))
    pygame.draw.arc(circle_surface, (0, 0, 255), circle_surface.get_rect(), 0, 2 * pi)
    win.blit(circle_surface, (200, 300))


def draw_centered_circle():
    x, y = 200, 200

    print(100 * math.sin(1), 100 * math.cos(1))
    radius_1 = 100
    radius_2 = 2
    pygame.draw.circle(win, (0, 0, 0), (x, y), 6, 1)
    pygame.draw.circle(win, (255, 255, 255), (x, y - 100), 6, 1)


    pygame.draw.line(win, (255, 255, 255), (x, y), (x, y - radius_1), 2)

while running:
    #draw_centered_circle()
    draw_circle()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

