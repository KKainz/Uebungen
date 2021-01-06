import abc
from typing import List, Dict


class Fluessigkeit():

    def __init__(self, name: str, menge: float, alkohol_prozent:float):
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

    def __repr__(self):
        return f'Name des Getränkes: {self.name}, Zutaten: {self.get_anzahl_zutaten()}, alkoholisch: ' \
               f'{self.beinhaltet_alkohol()}, brennbar: {self.brennt()}'

    @abc.abstractmethod
    def get_anzahl_zutaten(self) -> int:
        pass

    @abc.abstractmethod
    def beinhaltet_alkohol(self) -> bool:
        pass

    @abc.abstractmethod
    def menge_in_ml(self) ->float:
        pass

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
        super().__init__(name)
        self.spirituose = spirituose
        self.filler = filler

    def get_anzahl_zutaten(self) -> int:
        return 2

    def beinhaltet_alkohol(self) -> bool:
        if self.spirituose.alkohol_prozent > 0:
            return True
        else:
            return False

    def menge_in_ml(self) -> float:
        return self.spirituose.menge + self.filler.menge

    def brennt(self) -> bool:
        if self.spirituose.alkohol_prozent > 30:
            return True
        else:
            return False

class Cocktail(Getraenk):

    def __init__(self, name: str, bestandteile: List[Fluessigkeit]):
        super().__init__(name)
        self.bestandteile = bestandteile

    def get_anzahl_zutaten(self) -> int:
        return len(self.bestandteile)

    def beinhaltet_alkohol(self) -> bool:
        for b in self.bestandteile:
            if b.alkohol_prozent > 0:
                return True
            else:
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
            else:
                return False

class Registrierkasse():

    def __init__(self):
        self.__drinks = []
        self.__verkaufte_getraenke = 0

    def verkauft(self, g: Getraenk):
        self.__drinks.append(g)
        self.__verkaufte_getraenke += 1

    def getraenke_aufgeteilt_nach_zutaten(self) -> Dict[int, List[Getraenk]]:
        karte = {}
        for d in self.__drinks:
            x = d.get_anzahl_zutaten()
            if x in karte:
                karte[x].append(d.name)
            else:
                karte[x] = [d.name]
        return karte


if __name__ == '__main__':

    rb = Fluessigkeit("Red Bull", 250, 0)
    wrot = Fluessigkeit("Wodka (rot)", 20, 32)
    osaft = Fluessigkeit("Orangensaft", 250, 0)
    cola = Fluessigkeit("Cola", 250, 0)
    teq = Fluessigkeit("Tequila", 20, 40)
    wwein = Fluessigkeit("Weisswein", 125, 10)
    soda = Fluessigkeit("Soda", 125, 0)
    gre = Fluessigkeit("Grenadine", 40, 0)
    kassa = Registrierkasse()

    os = SimplesGetraenk("Orangensaft", osaft)
    colaw = LongDrink("Cola Weiss", wwein, cola)
    print(colaw.brennt())
    print(colaw.beinhaltet_alkohol())
    print(colaw.get_anzahl_zutaten())

    teqs = Cocktail("Tequila Sunrise", [teq, gre, osaft])
    print(teqs.get_anzahl_zutaten())
    print(teqs.beinhaltet_alkohol())
    print(teqs.brennt())

    kassa.verkauft(teqs)
    kassa.verkauft(colaw)
    kassa.verkauft(os)
    print(kassa.getraenke_aufgeteilt_nach_zutaten())
    print(kassa._Registrierkasse__drinks)
    
