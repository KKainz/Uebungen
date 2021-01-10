import abc
from typing import List, Dict

#1 - Enten

class Ente(abc.ABC):

    def __init__(self, name: str, gewicht: int):
        self._name = name
        self._gewicht = gewicht

    @property
    def name(self):
        return self._name

    @property
    def gewicht(self):
        return self._gewicht

    @abc.abstractmethod
    def get_full_weight(self) -> int:
        pass

    @abc.abstractmethod
    def make_noise(self) -> str:
        pass

class FlugEnte(Ente):

    def __init__(self, name: str, gewicht: float, gewicht_federn: int):
        super().__init__(name, gewicht)
        self.gewicht_federn = gewicht_federn

    def __repr__(self):
        return f'{self._name}: Gewicht {self._gewicht}g, Gewicht Federn {self.gewicht_federn}g'

    def get_full_weight(self) -> int:
        return self._gewicht + self.gewicht_federn

    def make_noise(self) -> str:
        return f'Quack quack'

class BadeEnte(Ente):

    def __init__(self, name: str, gewicht: float, gewicht_wasser: int):
        super().__init__(name, gewicht)
        self.gewicht_wasser = gewicht_wasser

    def __repr__(self):
        return f'{self._name}: Gewicht {self._gewicht}g, Gewicht Federn {self.gewicht_wasser}g'

    def get_full_weight(self) -> int:
        return self.gewicht + self.gewicht_wasser

    def make_noise(self) -> str:
        return f'Quietsch quietsch'

class Entenhausen:

    def __init__(self):
        self.__enten_liste = []

    def add(self, ente: Ente):
        return self.__enten_liste.append(ente)

    def get_gruppierte_enten(self) -> Dict[int, List[Ente]]:
        enten_dict = {100: [], 200: [], 300: []}
        for e in self.__enten_liste:
            h = e.get_full_weight()
            if h <= 100:
                enten_dict.get(100).append(e)
            elif 100 < h <= 200:
                enten_dict.get(200).append(e)
            elif 200 < h <= 300:
                enten_dict.get(300).append(e)
        return enten_dict

# 2 - Getraenke

class Fluessigkeit:

    def __init__(self, name: str, menge: float, alkohol_prozent: float):
        self.name = name
        self.menge = menge
        self.alkohol_prozent = alkohol_prozent

class Brennbar(abc.ABC):

    @abc.abstractmethod
    def brennt(self) -> bool:
        pass

class Getraenk(Brennbar, abc.ABC):

    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def get_anzahl_zutaten(self) -> int:
        pass

    @abc.abstractmethod
    def beinhaltet_alkohol(self) -> bool:
        pass

    @abc.abstractmethod
    def menge_in_ml(self) -> float:
        pass

    def __repr__(self):
        return f'{self.name}, Zutaten: {self.get_anzahl_zutaten()}, alkoholisch: {self.beinhaltet_alkohol()}, brennbar: {self.brennt()}'

class SimplesGetraenk(Getraenk):

    def __init__(self, name: str, bestandteil: Fluessigkeit):
        super().__init__(name)
        self.bestandteil = bestandteil

    def get_anzahl_zutaten(self) -> int:
        return 1

    def beinhaltet_alkohol(self) -> bool:
        if self.bestandteil.alkohol_prozent > 0:
            return True
        else:
            return False

    def menge_in_ml(self) -> float:
        return self.bestandteil.menge

    def brennt(self) -> bool:
        if self.bestandteil.alkohol_prozent > 30:
            return True
        else:
            return False

class LongDrink(Getraenk):

    def __init__(self, name: str, spirituose: Fluessigkeit, filler: Fluessigkeit):
        self.name = name
        self.spirituose = spirituose
        self.filler = filler

    def get_anzahl_zutaten(self) -> int:
        return 2

    def beinhaltet_alkohol(self) -> bool:
        if self.spirituose.alkohol_prozent > 0 or self.filler.alkohol_prozent > 0:
            return True
        else:
            return False

    def menge_in_ml(self) -> float:
        return self.spirituose.menge + self.filler.menge

    def brennt(self) -> bool:
        if self.spirituose.alkohol_prozent > 30 or self.filler.alkohol_prozent > 30 :
            return True
        else:
            return False

class Cocktail(Getraenk):

    def __init__(self, name: str, bestandteile: List[Fluessigkeit]):
        self.name = name
        self.bestandteile = bestandteile

    def get_anzahl_zutaten(self) -> int:
        return len(self.bestandteile)

    def beinhaltet_alkohol(self) -> bool:
        for b in self.bestandteile:
            if b.alkohol_prozent > 0:
                return True
        return False

    def menge_in_ml(self) -> float:
        m = 0
        for b in self.bestandteile:
            m += b.menge
        return m

    def brennt(self) -> bool:
        for b in self.bestandteile:
            if b.alkohol_prozent > 30:
                return True
        return False

class Registrierkasse:

    def __init__(self):
        self.__getraenke_liste = []
        self.__verkaufte_getraenke = 0


    def verkauft(self, g: Getraenk):
        self.__verkaufte_getraenke += 1
        self.__getraenke_liste.append(g)

    # def getraenke_sortiert_nach_anzahl_zutaten(self):

    def getraenke_aufgeteilt_nach_zutaten(self) -> Dict[int, List[Getraenk]]:
        zut = {}
        for g in self.__getraenke_liste:
            anz = g.get_anzahl_zutaten()
            zut.setdefault(anz, []).append(g)
        return zut

if __name__ == '__main__':
    o = Fluessigkeit("Orangensaft", 250, 0)
    c = Fluessigkeit("Cola", 250, 0)
    g = Fluessigkeit("Grenadine", 40, 0)
    r = Fluessigkeit("Rum", 20, 33)
    w = Fluessigkeit("Whisky", 20, 33)
    t = Fluessigkeit("Tequila", 20, 33)
    m = Fluessigkeit("Minze", 40, 0)
    rt = Fluessigkeit("Rotwein", 250, 12)

    osaft = SimplesGetraenk("O-Saft", o)
    colar = LongDrink("Cola Rot", rt, c)
    wc = LongDrink("Whisky Cola", w, c)
    teq = Cocktail("Tequila Sunrise", [o, g, t])
    rum = Cocktail("Rummi", [c, r, m])
    kassa = Registrierkasse()

    print(teq.brennt())

    kassa.verkauft(osaft)
    kassa.verkauft(rum)
    kassa.verkauft(teq)
    kassa.verkauft(wc)
    kassa.verkauft(colar)

    print(kassa.getraenke_aufgeteilt_nach_zutaten())





    a = BadeEnte("Donald", 200, 80)
    t1 = BadeEnte("Tick", 75, 30)
    t2 = BadeEnte("Trick", 80, 30)
    t3 = BadeEnte("Track", 70, 30)
    b = FlugEnte("Bertl", 150, 55)
    d = FlugEnte("Daisy", 165, 30)
    dag = Entenhausen()

    dag.add(a)
    dag.add(t1)
    dag.add(t2)
    dag.add(t3)
    dag.add(b)
    dag.add(d)

    print(dag.get_gruppierte_enten())

