import time
from Game import *


def main():

    Game().main_loop()
    time.sleep(1)
    pygame.quit()


if __name__ == '__main__':
    main()
