import pygame

from tiles import Tile
from player import Player
from settings import tile_size, screen_width

class Level():
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0


    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_i, row in enumerate(layout):
            for col_i, col in enumerate(row):
                x = col_i*tile_size
                y = row_i*tile_size

                # x marks platform
                if col == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif col == "P":
                    player = Player((x, y))
                    self.player.add(player)

    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x > (screen_width * 0.9) and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        elif player_x < (screen_width * 0.1) and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 5


    def run(self):
        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()
        self.player.draw(self.display_surface)

        self.scroll_x()
    