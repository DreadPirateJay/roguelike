from map_objects.tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(False) for y in range(self.height)]
                 for x in range(self.width)]

        tiles[30][32].blocked = True
        tiles[30][32].block_sight = True
        tiles[31][32].blocked = True
        tiles[31][32].block_sight = True
        tiles[32][32].blocked = True
        tiles[32][32].block_sight = True

        return tiles

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
