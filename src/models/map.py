class Map:
    def __init__(self, map_data):
        self.data = map_data

    def get_terrain(self, pos):        
        return self.data[pos]["terrain"]