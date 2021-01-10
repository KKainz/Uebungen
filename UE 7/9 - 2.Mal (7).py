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
    def category(self):
        return int(self.__square_meter / 10)

    @abc.abstractmethod
    def calc_lease(self) -> float:
        pass

    def __repr__(self):
        return f'{self.__square_meter} m2'

class Office(RealEstate):

    def __init__(self, square_meter: float, people: int):
        super().__init__(square_meter)
        self.__people = people

    def calc_lease(self) -> float:
        lease = 0
        if self.__people < 50:
            lease = self.square_meter * 8
        elif 50 <= self.__people < 100:
            lease = self.square_meter * 8.2 + 90
        elif self.__people >= 100:
            lease = self.square_meter * 8.5 + self.__people
        return lease

    def __repr__(self):
        return f'{self.square_meter} for {self.__people} people'

class Flat(RealEstate):

    def __init__(self, square_meter: float, count_room: int, type: str):
        super().__init__(square_meter)
        self.__count_room = count_room
        self.__type = type

    def __repr__(self):
        return f'{self.square_meter}, {self.__count_room} rooms, {self.__type}'

    def calc_lease(self) -> float:
        lease = 0
        if self.__type == 'Low':
            lease = self.square_meter * 7
        elif self.__type == 'Standard':
            lease = self.square_meter * 7.5 + self.__count_room * 10
        elif self.__type == 'High':
            lease = self.square_meter * 8 + self.__count_room * 12
        else:
            return -1
        return lease

class House(RealEstate):

    def __init__(self, square_meter: float, garden: bool):
        super().__init__(square_meter)
        self.__garden = garden

    def __repr__(self):
        return f'{self.square_meter}, garden: {self.__garden}'

    def calc_lease(self) -> float:
        lease = 0
        if self.__garden:
            lease = self.square_meter * 10 + 200
        else:
            lease = self.square_meter * 15
        if lease < 1000:
            lease = 1000
        return lease

class Accounting:

    def __init__(self):
        self.__real_estates = []

    def add(self, re: RealEstate):
        self.__real_estates.append(re)

    def print_all(self):
        for r in self.__real_estates:
            print(r)

    def get_overall_lease(self) -> float:
        sum = 0
        for r in self.__real_estates:
            sum += r.calc_lease()
        return sum

    def get_average_lease(self) -> float:
        avg = 0
        for r in self.__real_estates:
            avg += r.calc_lease()
        return avg / len(self.__real_estates)

    def get_real_estate_in_category(self) -> Dict[int, int]:
        cat_dict = {}
        for r in self.__real_estates:
            cat = r.category
            cat_dict[cat] = 1 + cat_dict.get(cat, 0)
        return cat_dict


if __name__ == '__main__':
    a = Office(500, 45)
    b = Flat(85, 3, "High")
    c = House(135, True)
    acc = Accounting()

    acc.add(a)
    acc.add(b)
    acc.add(c)
    acc.print_all()
    print(acc.get_overall_lease())
    print(acc.get_average_lease())
    print(acc.get_real_estate_in_category())


