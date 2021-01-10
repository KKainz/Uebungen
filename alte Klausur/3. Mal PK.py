from typing import List, Dict
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
        return f'Verscheucht: {self.verscheuche_raeuber()}, Musiziert: {self.spiele_musik()}'

class Esel(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, tritt_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__tritt_kraft = tritt_kraft

    def __repr__(self):
        return f'{type(self).__name__} {self.__tritt_kraft}: {super().__repr__()}'

    def verscheuche_raeuber(self) -> int:
        return math.floor(self.__tritt_kraft * self.anzahl_beine)

    def spiele_musik(self) -> float:
        return self.instrument.lautstaerke

class Hund(Musikant):

    def __init__(self, anzahl_beine: int, instrument: Instrument, bell_lautstaerke: float):
        super().__init__(anzahl_beine, instrument)
        self.__bell_lautstaerke = bell_lautstaerke

    def __repr__(self):
        return f'{type(self).__name__} {self.__bell_lautstaerke}: {super().__repr__()}'

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

    def __repr__(self):
        return f'{type(self).__name__} {self.__kratz_kraft}: {super().__repr__()}'

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

    def __repr__(self):
        return f'{type(self).__name__} {self.__flug_weite}: {super().__repr__()}'

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

    def add(self, m: Musikant):
        self.__musikanten_liste.append(m)

    def ist_quartett(self) -> bool:
        if len(self.__musikanten_liste) == 4:
            return True
        else:
            return False

    def gemeinsam_raeuber_verscheucht(self) -> int:
        ver = 0
        for r in self.__musikanten_liste:
            ver += r.verscheuche_raeuber()
        return ver

    def durchschnittliche_lautstaerke(self) -> float:
        vol = 0
        for laut in self.__musikanten_liste:
            vol += laut.spiele_musik()
        erg = vol / len(self.__musikanten_liste)
        return erg

    def get_musikanten_in_laustaerke_bereich(self, von: float, bis: float) -> List[Musikant]:
        bereich = []
        for m in self.__musikanten_liste:
            if m.spiele_musik() >= von and m.spiele_musik() <= bis:
                bereich.append(m)
        return bereich

    def get_anzahl_musikanten_mit_bein_anzahl(self) -> Dict[int, int]:
        bein_dict = {}
        for b in self.__musikanten_liste:
            anzahl = bein_dict.get(b.anzahl_beine, 0) + 1
            bein_dict[b.anzahl_beine] = anzahl
        return bein_dict


#        for b in range(len(self.__musikanten_liste)):
#            if self.__musikanten_liste[b] in bein_dict:
#                bein_dict[self.__musikanten_liste[b].anzahl_beine] += 1
#            else:
#                bein_dict[self.__musikanten_liste[b].anzahl_beine] = 1
#        return bein_dict




if __name__ == '__main__':
    chello = Instrument("Chello", 5)
    klavier = Instrument("Klavier", 6)
    floete = Instrument("Floete", 4)
    drum = Instrument("Schlagzeug", 8)

    esel = Esel(4, chello, 6.5)
    hund = Hund(4, klavier, 5.9)
    katze = Katze(3, floete, 8.2)
    hahn = Hahn(2, drum, 3)

    q = Quartett()
    q.add(esel)
    q.add(hahn)
    q.add(hund)
    q.add(katze)

    print(q.ist_quartett())
    print(q.gemeinsam_raeuber_verscheucht())
    print(q.durchschnittliche_lautstaerke())
    print(q.get_musikanten_in_laustaerke_bereich(5, 10))
    print(q.get_anzahl_musikanten_mit_bein_anzahl())