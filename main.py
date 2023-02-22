import pygame

from sys import exit
from settings import *
from level import Level


def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.fill("black")
        level.run()

        # update scrin
        pygame.display.update()
        # 60 fps boi
        game_clock.tick(60)


if __name__ == '__main__':
    # inits bruv
    pygame.init()
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    game_clock = pygame.time.Clock()
    level = Level(level_map, screen)

    game()
