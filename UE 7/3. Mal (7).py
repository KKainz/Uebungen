import abc
from typing import List, Dict

class RoomOpening(abc.ABC):

    def __init__(self, posx: float, posy: float, width: float, length: float):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.length = length

class Window(RoomOpening):

    def __init__(self, posx: float, posy: float, width: float, length: float, can_be_opened: bool):
        super().__init__(posy, posx, width, length)
        self.can_be_opened = can_be_opened

class Door(RoomOpening):

    def __init__(self, posx: float, posy: float, width: float, length: float, room1: Room, room2: Room):
        super().__init__(posy, posx, width, length)
        self.room1 = room1
        self.room2 = room2

class HouseDoor(Door):

    def __init__(self, posx: float, posy: float, width: float, length: float, room1: Room, room2=None, security_door: bool):
        super().__init__(posy, posx, width, length, room1, room2)
        self.security_door = security_door

class BalconyDoor(Door):

    def __init__(self, posx: float, posy: float, width: float, length: float, room1: Room, room2=None, tiltable: bool):
        super().__init__(posy, posx, width, length, room1, room2)
        self.tiltable = tiltable

class Room:

    TYPE_VALID = {'BEDROOM', 'KITCHEN', 'LIVINGROOM', 'EATINKITCHEN', 'STOREROOM', 'TOILET', 'BATHROOM', 'TOILET', 'CORRIDOR'}
    ORIENTATION_VALID = {'EAST', 'NORTH', 'SOUTH', 'WEST'}

    def __init__(self, type: str, area: float):
        self.type = type
        self.area = area
        self.openings = {}
        self.openings = Dict[str, List[RoomOpening]]

    def __repr__(self):
        return f'{self.type}, {self.area} sqm.'

    def add_opening(self, orientation: str, roomopening: RoomOpening):
        if self.orientation not in self.ORIENTATION_VALID:
            raise ValueError('Type not valid')
        if orientation in self.openings:
            self.openings[orientation].append(roomopening)
        else:
            self.openings[orientation] = [roomopening]

class House:

    def __init__(self):
        self.rooms = {}
        self.rooms = Dict[str, List[Room]]

    def add_room(self, room: Room):
        if room in self.rooms:
            self.rooms[room.type].append(room)
        else:
            self.rooms[room.type] = [room]

    def get_window_area_facing_orientation(self, orientation: str) -> float:
        n = 0
        for x in self.rooms.values():
            for y in x:
                for key, value in y.openings.items():
                    if key == orientation:
                        for v in value:
                            if isinstance(v, Window):
                                n += len(v)
        return n

    def get_number_of_openings_in_room_type(self, type: str) -> int:
        n = 0
        for x in self.rooms[type]:
            for y in x.openings.value():
                n += len(y)
        return n

    def get_all_connected_rooms(self, room: Room) -> List[Room]:
        rooms_con = []












if __name__ == '__main__':
    pass