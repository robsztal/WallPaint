import pytest
from rooms import House, Room


class TestHouseCreation:
    def test_one_room(self):
        house = House(1)
        house.add_room(True, 4)

        house.rooms[0].add_wall(400, 300)
        assert house.rooms[0].walls[0].area == 120000

        house.rooms[0].walls[0].set_paint("decoral")
        assert house.rooms[0].walls[0].paint_required == 12