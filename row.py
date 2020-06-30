
from tile import Tile

class Row:

    # rows are 0-8 to represent overall grid location
    
    def __init__(self, row, tiles):

        self.row = row

        self.tiles = []
        for tile in tiles:
            self.tiles.append(tile)

    def getRow(self):
        return self.tiles

    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.draw()

