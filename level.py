import pygame

from tiles import Tile
from settings import tile_size

class Level():
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0


    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()

        for row_i, row in enumerate(layout):
            for col_i, col in enumerate(row):
                if col == "X":
                    x = col_i*tile_size
                    y = row_i*tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)


    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
