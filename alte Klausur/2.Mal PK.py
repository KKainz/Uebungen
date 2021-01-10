from typing import Dict, List
import abc
import math

class Instrument:

    def __init__(self, name: str, lautstaerke: float):
        self.name = name
        self.lautstaerke = lautstaerke

class Musikant(abc.ABC):

        def __init__(self, anzahl_beine: int, instrument: Instrument):
            self.__anzahl_beine = anzahl_beine
            self.__instrument = instrument

        @property
        def anzahl_beine(self):
            return self.__anzahl_beine

        @property
        def instrument(self):
            return self.__instrument

        @abc.abstractmethod
        def verscheuche_raeuber(self) -> int:
            pass

        @abc.abstractmethod
        def spiele_musik(self) -> float:
            pass

        def __repr__(self):
            return f'Verscheucht: {self.verscheuche_raeuber()}, musiziert: {self.spiele_musik()}'

class Esel(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, tritt_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__tritt_kraft = tritt_kraft

    @property
    def tritt_kraft(self):
        return self.__tritt_kraft

    def __repr__(self):
        return f'{type(self).__name__}, {self.__tritt_kraft}: {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        return math.floor(self.__tritt_kraft * self.anzahl_beine)

    def spiele_musik(self) -> float:
        return self.instrument.lautstaerke

class Hund(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, bell_lautstaerke: float):
        super().__init__(anzahl_beine, instrument)
        self.__bell_lautstaerke = bell_lautstaerke

    @property
    def bell_lautstaerke(self):
        return self.__bell_lautstaerke

    def __repr__(self):
        return f'{type(self).__name__}, {self.__bell_lautstaerke}: {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        if self.__bell_lautstaerke > self.instrument.lautstaerke:
            return math.floor(self.__bell_lautstaerke)
        else:
            return math.floor(self.instrument.lautstaerke)

    def spiele_musik(self) -> float:
        return (self.__bell_lautstaerke + self.instrument.lautstaerke) / 2

class Katze(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, kratz_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__kratz_kraft = kratz_kraft

    @property
    def kratz_kraft(self):
        return self.__kratz_kraft
    def __repr__(self):
        return f'{type(self).__name__}, {self.__kratz_kraft}: {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        if self.anzahl_beine == 3:
            return math.floor(self.__kratz_kraft / 2)
        elif self.anzahl_beine <= 2:
            return 1
        else:
            return math.floor(self.__kratz_kraft)

    def spiele_musik(self) -> float:
        return self.instrument.lautstaerke

class Hahn(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, flug_weite: int):
        super().__init__(anzahl_beine, instrument)
        self.__flug_weite = flug_weite

    @property
    def flug_weite(self):
        return self.__flug_weite

    def __repr__(self):
        return f'{type(self).__name__}, {self.__flug_weite}: {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        if self.__flug_weite < 2:
            return math.floor(self.instrument.lautstaerke)
        elif self.__flug_weite == 2:
            return 6
        elif self.__flug_weite == 3:
            return 5
        elif self.__flug_weite == 4:
            return 4
        elif self.__flug_weite == 5:
            return 3
        elif self.__flug_weite == 6:
            return 2
        else:
            return 1

    def spiele_musik(self) -> float:
        return (self.instrument.lautstaerke + 2) / self.__flug_weite

class Quartett:

    def __init__(self):
        self.__musikanten_liste = []

    def add(self, musikant: Musikant):
        self.__musikanten_liste.append(musikant)

    def ist_quartett(self) -> bool:
        if len(self.__musikanten_liste) == 4:
            return True
        else:
            return False

    def gemeinsam_raeuber_verscheucht(self) -> int:
        r = 0
        for m in self.__musikanten_liste:
            r += m.verscheuche_raeuber()
        return r

    def durchschnittliche_lautstaerke(self) -> float:
        v = 0
        for m in self.__musikanten_liste:
            v += m.spiele_musik()
        return v / len(self.__musikanten_liste)

    def get_musikanten_in_lautstaerke_bereich(self, von: float, bis: float) -> List[Musikant]:
        lb = []
        for n in self.__musikanten_liste:
            if von <= n.instrument.lautstaerke <= bis:
                lb.append(n)
        return lb

    def get_anzahl_musikanten_mit_bein_anzahl(self) -> Dict[int, int]:
        ba = {}
        for x in range(len(self.__musikanten_liste)):
            if self.__musikanten_liste[x].anzahl_beine in ba:
                ba[self.__musikanten_liste[x].anzahl_beine] += 1
            else:
                ba[self.__musikanten_liste[x].anzahl_beine] = 1
        return ba


if __name__ == '__main__':
    t = Instrument("Trommel", 6.5)
    s = Instrument("Saxophon", 4.8)
    b = Instrument("Banjo", 2.4)
    o = Instrument("Oboe", 5.1)

    e = Esel(4, t, 7.2)
    hu = Hund(4, s, 3.8)
    k = Katze(3, b, 8.1)
    ha = Hahn(2, o, 1.6)

    qua = Quartett()
    qua.add(e)
    qua.add(hu)
    qua.add(ha)
    qua.add(k)

    print(qua.ist_quartett())
    print(qua.gemeinsam_raeuber_verscheucht())
    print(qua.durchschnittliche_lautstaerke())
    print(qua.get_musikanten_in_lautstaerke_bereich(2, 36))
    print(qua.get_anzahl_musikanten_mit_bein_anzahl())