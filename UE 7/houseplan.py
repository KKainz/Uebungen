import abc
from typing import Dict, List

class RoomOpening(abc.ABC):

    def __init__(self, posx: float, posy: float, width: float, height: float):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

class Room:
    TYPE_VALID = {'Bedroom', 'Kitchen', 'Livingroom', 'Eatinkitchen', 'Storeroom', 'Toilet', 'Bathroom', 'Corridor'}
    ORIENTATION_VALID = {'North', 'East', 'South', 'West'}

    def __init__(self, type: str, area: float):
        self.type = type
        self.area = area
        self.openings = {}
        self.openings = Dict[str, List[RoomOpening]]
        if self.type not in Room.TYPE_VALID:
            raise ValueError('Room type not valid')

    def __repr__(self):
        return f'{self.type}:{self.area} m2'

    def add_opening(self, orientation: str, opening: RoomOpening):
        if self.orientation not in Room.ORIENTATION_VALID:
            raise ValueError('Orientation not valid')
        if orientation in self.openings:
            self.openings[orientation].append(opening)
        else:
            self.openings[orientation] = [opening]

class Window(RoomOpening):

    def __init__(self, posx: float, posy: float, width: float, height: float, can_be_opened: bool):
        super().__init__(posx, posy, width, height)
        self.can_be_opened = can_be_opened

class Door(RoomOpening):

    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, room2: Room):
        super().__init__(posx, posy, width, height)
        self.room1 = room1
        self.room2 = room2

class HouseDoor(Door):

    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, room2=None, security_door: bool):
        super().__init__(posx, posy, width, height, room1, room2)
        self.security_door = security_door


    #def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, room2=None, security_door: bool):
    #    super().__init__(posx, posy, width, height, room1, room2)
    #    self.security_door = security_door

class BalconyDoor(Door):

    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, room2=None,tiltable: bool):
        super().__init__(posx, posy, width, height, room1, room2)
        self.tiltable = tiltable

class House:

    def __init__(self):
        self.rooms = {}
        self.rooms = Dict[str, List[Room]]

    def add_room(self, room: Room):
        if room.type in self.rooms:
            self.rooms[room.type].append(room)
        else:
            self.rooms[room.type] = [room]

    def get_window_area_facing_orientation(self, orientation: str) -> float:
        w = 0
        for x in self.rooms.values():
            for y in x:
                for key, value in y.openings.items():
                    if key == orientation:
                        for v in value:
                            if isinstance(v, Window):
                                w += len(v)
        return w

    def get_number_of_openings_in_room_type(self, type: str) -> int:
        t = 0
        for x in self.rooms[type]:
            for y in x.openings.value():
                t += len(y)
        return t

    def get_all_connected_rooms(self, room: Room) -> List[Room]:
        connected_rooms = []
        for x in room.openings.values():
            for y in range(len(x)):
                if type(x[y]) == Door:
                    if z[v].room1 not in connected_rooms and z[v].room1 != room:
                        connected_rooms.append(z[v].room1)
                    if z[v].room2 not in connected_rooms and z[v].room2 != room:
                        connected_rooms.append(z[v].room2)
        return connected_rooms


if __name__ == '__main__':
    hallway = Room('Corridor', 7)
    hallway.add_opening('North', HouseDoor(10, 0, 110, 210, hallway, False))

    bedroom = Room('Bedroom', 17)
    bedroom.add_opening('East', Window(100, 100, 50, 50, True))
    bedroom.add_opening('East', Window(160, 160, 50, 50, True))

    livingroom = Room('Eatinkitchen', 25)
    livingroom.add_opening('West', BalconyDoor(100, 0, 100, 200, livingroom, True))
    livingroom.add_opening('West', Window(50, 50, 50 ,50, False))

    bath = Room('Bathroom', 9)
    bath.add_opening('East', Window(40, 150, 50, 20, True))

    wc = Room('Toilet', 3)
    wc.add_opening('North', Window(50, 50, 35, 35, True))

    d1 = Door(20, 0, 110, 200, hallway, bath)
    hallway.add_opening('West', d1)
    bath.add_opening('East', d1)

    d2 = Door(20, 0, 110, 200, hallway, bedroom)
    hallway.add_opening('South', d2)
    bedroom.add_opening('North', d2)

    d3 = Door(20, 0, 110, 200, hallway, livingroom)
    hallway.add_opening('East', d3)
    livingroom.add_opening('West', d3)

    d4 = Door(20, 0, 110, 200, hallway, wc)
    hallway.add_opening('East', d4)
    wc.add_opening('West', d4)

    h = House()
    h.add_room(bedroom)
    h.add_room(hallway)
    h.add_room(bath)
    h.add_room(kitchen)
    h.add_room(livingroom)
    h.add_room(wc)


