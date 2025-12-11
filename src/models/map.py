class Map:
    HEX_OFFSETS_ODD = [
        (0, -1),  # N
        (1, -1),  # NE
        (1, 0),  # SE
        (0, 1),  # S
        (-1, 0),  # SW
        (-1, -1),  # NW
    ]

    HEX_OFFSETS_EVEN = [
        (0, -1), # N
        (1, 0), # NE
        (1, 1), # SE
        (0, 1), # S
        (-1, 1), # SW
        (-1, 0) # NW
    ]

    def __init__(self, map_data):
        self.data = map_data

    def get_terrain(self, pos):
        return self.data[pos]["terrain"]

    def is_in_bounds(self, pos):
        x, y = pos
        return x > 0 and x < 21 and y < 24

    def get_valid_moves(self, pos):
        x, y = pos
        offsets = Map.HEX_OFFSETS_EVEN if x % 2 == 0 else Map.HEX_OFFSETS_ODD
        return [
                (x + dx, y + dy)
                for dx, dy in offsets
                if self.is_in_bounds((x + dx, y + dy))
            ]
