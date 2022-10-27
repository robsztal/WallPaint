from paints import paints_coverage


class StandardWall:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.paint = None
        self.paint_required = 0

    def set_paint(self, paint: str):
        self.paint = paint
        self.paint_required = self.area * paints_coverage[paint]

    def calculate_paint_required(self):
        self.paint_required = self.area * paints_coverage[self.paint]


class Room:
    def __init__(self, is_symetrical: bool, walls_num: int):
        self.is_symetrical = is_symetrical
        self.walls_num = walls_num
        self.walls = []
    
    def add_wall(self, width: int, height: int):
        self.walls.append(StandardWall(width, height))

class House:
    def __init__(self):
        self.rooms = {}

    def add_room(self, is_symetrical: bool, walls_num: int, room_name: str):
        self.rooms[room_name] = Room(is_symetrical, walls_num)