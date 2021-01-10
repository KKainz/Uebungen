import abc
from typing import List, Dict
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
        return f'Verscheucht: {self.verscheuche_raeuber()}, Musiziert: {self.spiele_musik()}'

class Esel(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, tritt_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__tritt_kraft = tritt_kraft

    @property
    def tritt_kraft(self):
        return self.__tritt_kraft

    def __repr__(self):
        return f'{type(self).__name__}, Trittkraft {self.tritt_kraft}: {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        e = math.floor(self.tritt_kraft * self.anzahl_beine)
        return e

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
        return f'{type(self).__name__}, {self.bell_lautstaerke}: {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        return 1

    def spiele_musik(self) -> float:
        return (self.instrument.lautstaerke + self.bell_lautstaerke) / 2

class Katze(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, kratz_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__kratz_kraft = kratz_kraft

    @property
    def kratz_kraft(self):
        return self.__kratz_kraft

    def __repr__(self):
        return f'{type(self).__name__}, {self.kratz_kraft}: {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        if self.anzahl_beine == 4:
            k = math.floor(self.kratz_kraft)
        elif self.anzahl_beine == 3:
            k = math.floor(self.kratz_kraft / 2)
        else:
            k = 1
        return k

    def spiele_musik(self) -> float:
        return self.instrument.lautstaerke

class Hahn(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, flug_weite: float):
        super().__init__(anzahl_beine, instrument)
        self.__flug_weite = flug_weite

    @property
    def flug_weite(self):
        return self.__flug_weite

    def __repr__(self):
        return f'{type(self).__name__}, {self.flug_weite}: {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        if self.flug_weite < 2:
            h = self.instrument.lautstaerke
        elif self.flug_weite == 2:
            h = 6
        elif self.flug_weite == 3:
            h = 5
        elif self.flug_weite == 4:
            h = 4
        elif self.flug_weite == 5:
            h = 3
        elif self.flug_weite == 6:
            h = 2
        else:
            h = 1
        return math.floor(h)

    def spiele_musik(self) -> float:
        return (self.instrument.lautstaerke + 2) / self.flug_weite

class Quartett:

    def __init__(self):
        self.__musikanten = []

    def add(self, musikant: Musikant):
        self.__musikanten.append(musikant)

    def ist_quartett(self) -> bool:
        if len(self.__musikanten) == 4:
            return True
        else:
            return False
        # return len(self.__musikanten) == 4

    def gemeinsam_raeuber_verscheucht(self) -> int:
        x = 0
        for y in range(len(self.__musikanten)):
            x += self.__musikanten[y].verscheuche_raeuber()
        return f'{x} Raeuber gemeinsam verscheucht'

    def durchschnittliche_lautstaerke(self) -> float:
        z = 0
        for x in range(len(self.__musikanten)):
            z += self.__musikanten[x].spiele_musik()
        y = z / len(self.__musikanten)
        return f'durchschnittliche Lautstärke: {y}'

    def get_musikante_in_lautstaerke_bereich(self, von: float, bis: float) -> List[Musikant]:
        liste_ls = []
        for x in range(len(self.__musikanten)):
            if von <= self.__musikanten[x].spiele_musik() <= bis:
                liste_ls.append(self.__musikanten[x])
        return liste_ls

    def get_anzahl_musikanten_mit_bein_anzahl(self) -> Dict[int, int]:
        beindict = {}
        for x in range(len(self.__musikanten)):
            if self.__musikanten[x].anzahl_beine in beindict:
                beindict[self.__musikanten[x].anzahl_beine] += 1
            else:
                beindict[self.__musikanten[x].anzahl_beine] = 1
        return beindict


if __name__ == '__main__':
    horn = Instrument('Horn', 5)
    floete = Instrument('Flöte', 6)
    git = Instrument('Gitarre', 4)
    trommel = Instrument('Trommel', 8)

    esel = Esel(4, horn, 6.5)
    hund = Hund(4, git, 5.9)
    katze = Katze(3, floete, 8.2)
    hahn = Hahn(2, trommel, 3)

    qua = Quartett()
    qua.add(katze)
    qua.add(hund)
    qua.add(hahn)
    qua.add(esel)

    print(qua.ist_quartett())
    print(qua.gemeinsam_raeuber_verscheucht())
    print(qua.durchschnittliche_lautstaerke())
    print(qua.get_musikante_in_lautstaerke_bereich(4, 8))
    print(qua.get_anzahl_musikanten_mit_bein_anzahl())