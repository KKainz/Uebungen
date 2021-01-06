import abc
from typing import List, Dict

class RealEstate(abc.ABC):

    def __init__(self, square_meter: float):
        self.__square_meter = square_meter

    @property
    def square_meter(self):
        return self.__square_meter

    @square_meter.setter
    def square_meter(self, value):
        self.__square_meter = value

    @property
    def category(self) -> int:
        return int(self.__square_meter / 10)

    @abc.abstractmethod
    def calc_lease(self) -> float:
        pass

    def __repr__(self):
        return f'Real Estate: {self.__square_meter} m2'

class Office(RealEstate):

    def __init__(self, square_meter: float, people: int):
        super().__init__(square_meter)
        self.__people = people

    def __repr__(self):
        return f'Office: {self.square_meter} m2 for {self.__people} people'

    def calc_lease(self) -> float:
        if self.__people < 50:
            return self.square_meter * 8
        elif self.__people >= 50 and self.__people < 100:
            return self.square_meter * 8.2 + 90
        elif self.__people >= 100:
            return self.square_meter * 8.5 + self.__people

class Flat(RealEstate):

    def __init__(self, square_meter: float, count_room: int, type: str):
        super().__init__(square_meter)
        self.__count_room = count_room
        self.__type = type

    def __repr__(self):
        f'Flat: {self.square_meter} m2, {self.__count_room} rooms, {self.__type}'

    def calc_lease(self) -> float:
        if self.__type == "low":
            return self.square_meter * 7
        elif self.__type == "standard":
            return self.square_meter * 7.5 + self.__count_room * 10
        elif self.__type == "high":
            return self.square_meter * 8 + self.__count_room * 12
        else:
            return -1

class House(RealEstate):

    def __init__(self, square_meter: float, garden: bool):
        super().__init__(square_meter)
        self.__garden = garden

    def __repr__(self):
        return f'House: {self.square_meter} m2, garden: {self.__garden}'

    def calc_lease(self) -> float:
        if self.__garden:
            m = self.square_meter * 10 + 200
        else:
            m = self.square_meter * 15

        if m < 1000:
            return 1000

        return m

class Accounting:

    def __init__(self):
        self.__real_estates = []

    def add(self, re: RealEstate):
        self.__real_estates.append(re)

    def print_all(self):
        for r in self.__real_estates:
            print(r)

    def get_overall_lease(self) -> float:
        s = 0
        for le in self.__real_estates:
            s += le.calc_lease()
        return s

    def get_average_lease(self) -> RealEstate:
        s = 0
        for le in self.__real_estates:
            s += le.calc_lease()
        return s / len(self.__real_estates)

    def get_real_estate_in_category(self) -> Dict[int, int]:
        immo = {}
        for i in self.__real_estates:
            if i.category in immo:
                immo[i.category] += 1
            else:
                immo[i.category] = 1
        return immo

if __name__ == '__main__':
    wohnung = Flat(88, 3, "high")
    buero = Office(500, 45)
    haus = House(150, True)

    print(wohnung.calc_lease())
    print(haus.calc_lease())
    print(buero.calc_lease())
    print(buero.category)

    acc = Accounting()

    acc.add(wohnung)
    acc.add(buero)
    acc.add(haus)

    print(acc.get_average_lease())
    print(acc.get_overall_lease())
    print(acc.get_real_estate_in_category())