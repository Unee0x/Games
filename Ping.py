from GameObject import *


class Ping(GameObject):

    def __init__(self):
        GameObject.__init__(self)
        self.surface = pygame.Surface((100, 20))
        self.surface_rect = self.surface.get_rect()
        self.surface_rect.center = self.window_rect.centerx, 500
        self.color = pygame.Color("white")
        self.surface.fill(self.color)
        self.init = False
        self.x_yel = 10

    def render(self):
        self.update()
        self.window.blit(self.surface, (self.surface_rect.x, self.surface_rect.y))

    def check_collisions(self):
        p = self.surface_rect
        w = self.window_rect

        if p.x <= 0:
            p.left = 0

        if p.right >= w.right:
            p.right = 600

    def update(self):

        if self.init:

            if self.key_event[pygame.K_LEFT]:
                self.surface_rect.centerx += -self.x_yel

            if self.key_event[pygame.K_RIGHT]:
                self.surface_rect.centerx += self.x_yel

