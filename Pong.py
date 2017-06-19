from GameObject import *


class Pong(GameObject):

    def __init__(self):
        GameObject.__init__(self)
        self.surface = pygame.Surface((10, 10))
        self.surface_rect = self.surface.get_rect()
        self.surface_rect.center = self.window_rect.center
        self.color = pygame.Color("white")
        self.init = False
        self.x_vel = random.randrange(-7, 7)
        self.y_vel = 9.8

    def render(self):
        pygame.draw.circle(self.window, self.color, (self.surface_rect.x, self.surface_rect.y), 10)
        self.update()

    def check_collisions(self):
        p = self.surface_rect
        w = self.window_rect

        if p.left <= 10:
            self.x_vel = -self.x_vel
        if p.right >= w.right - 10:
            self.x_vel = -self.x_vel
        if p.bottom <= 10:
            self.y_vel = -self.y_vel

    def update(self):
        if self.init:
            self.surface_rect.x += self.x_vel
            self.surface_rect.y += self.y_vel


