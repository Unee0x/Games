import pygame
import random


class GameObject:

    def __init__(self):

        self.window = pygame.display.set_mode((800, 600))
        self.window_rect = self.window.get_rect()
        self.surface = pygame.Surface((0, 0))
        self.surface_rect = self.surface.get_rect()
        self.color = None
        self.key_event = pygame.key.get_pressed()

    def render(self):
        pass

