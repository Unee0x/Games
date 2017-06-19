import sys
from Pong import *
from Ping import *


color = ['red', 'blue', 'yellow', 'magenta', 'purple', 'green', 'cyan', 'pink', 'orange', 'brown']

pygame.font.init()


class Game:

    def __init__(self):

        self.wall = self.my_wall()
        self.game_state = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.pong = Pong()
        self.pong.color = pygame.Color(color[random.randrange(0, 10)]) 
        self.ping = Ping()
        self.brick_hit = False
        self.points = 0
        self.slot = {}
        self.level()
        self.i = 0

    def render(self):
        display = pygame.display.get_surface()
        background = pygame.Surface(display.get_size())
        display.blit(background, (0, 0))
        self.check_collisions()
        self.pong.render()
        self.ping.render()
        self.draw_bricks()
        self.load_start_message()
        pygame.display.flip()

    def level(self):
        i = 0
        random.shuffle(color)
        for x in range(0, 8):
            for y in range(0, 1):
                self.slot[(x, y)] = color[i]
                i += 1

    def event_loop(self):

        self.clock.tick(self.fps)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()

            if ev.type in (pygame.KEYDOWN, pygame.KEYUP):
                self.pong.key_event = pygame.key.get_pressed()
                self.ping.key_event = pygame.key.get_pressed()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    self.ping.init = True
                    self.pong.init = True

    def draw_bricks(self):
        d = pygame.display.get_surface()
        for b in self.wall:
            if b:
                clr = pygame.Color(self.slot[int(b[0]/100), 0])

                pygame.draw.rect(d, clr, b)

        if len(self.wall) == 0:
            self.load_you_won_messege()

    def my_wall(self):
        my_wall = []
        for x in range(1, 7):
            for y in range(2, 10, 2):
                rect = pygame.Rect((x * 100,  y * 20, 100, 20))
                my_wall.append(rect)
        return my_wall

    def check_collisions(self):

        disp = pygame.display.get_surface()
        d = disp.get_rect()
        a = self.pong.surface_rect
        b = self.ping.surface_rect

        if a.x < 10 or a.x >= d[2] - 10:

            self.pong.x_vel = -self.pong.x_vel
            print(1)

        if a.top <= 0:
            self.pong.y_vel = -self.pong.y_vel
            print(2)

        if a.colliderect(b):
            self.pong.y_vel = -self.pong.y_vel
            print(3)

        if b.x <= 0:
            b.x = 1

        if b.right >= 800:
            b.right = 799

        if a.bottom > b.bottom:
            print('GameOver!')
            self.load_game_over_message()

        for x in self.wall:
            if a.colliderect(x):
                a.top = x.bottom + 10
                self.pong.y_vel = -self.pong.y_vel
                self.wall.remove(x)
                self.points += 10

    def load_start_message(self):

        display = pygame.display.get_surface()

        if not self.pong.init:

            font = pygame.font.SysFont("Menlo", 80)

            text = font.render("Push Space to Start", True, (255, 255, 255))

            display.blit(text, (125, 200))

    def load_game_over_message(self):

        display = pygame.display.get_surface()

        font = pygame.font.SysFont("Menlo", 120)

        text = font.render("Game Over !!!", True, (255, 0, 0))

        display.blit(text, (125, 200))
        self.game_state = False

    def load_you_won_messege(self):

        display = pygame.display.get_surface()

        font = pygame.font.SysFont("Menlo", 80)

        text = font.render("Congrats, You Won!!!", True, (0, 0, 255))

        display.blit(text, (125, 200))
        self.game_state = False

    def main_loop(self):

        while self.game_state:
            pygame.display.set_caption('Points: {}'.format(self.points))
            self.render()
            self.event_loop()


