class Map:
    HEX_OFFSETS = [
        (0, -1),  # N
        (1, -1),  # NE
        (1, 0),  # SE
        (0, 1),  # S
        (-1, 0),  # SW
        (-1, -1),  # NW
    ]

    def __init__(self, map_data):
        self.data = map_data

    def get_terrain(self, pos):
        return self.data[pos]["terrain"]

    def is_in_bounds(self, pos):
        x, y = pos
        return x > 0 and x < 21 and y < 23

    def get_valid_moves(self, pos):        
        x, y = pos
        valid = [(x + dx, y + dy) for dx, dy in Map.HEX_OFFSETS if self.is_in_bounds((x + dx, y + dy))]        
        return valid    