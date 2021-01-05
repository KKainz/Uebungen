from typing import List, Dict

class Zutat:

    def __init__(self, name: str, menge: int):
        self.__name = name
        self.__menge = menge

    @property
    def name(self):
        return self.__name

    @property
    def menge(self):
        return self.__menge
    def __repr__(self):
        return f'{self.name}: {self.menge}'

class Rezept:

    def __init__(self, name: str, personen: int, zutaten: List[Zutat]):
        self.__name = name
        self.__personen = personen
        self.__zutaten = zutaten

    @property
    def name(self):
        return self.__name

    @property
    def personen(self):
        return self.__personen

    @property
    def zutaten(self):
        return self.__zutaten

    def __str__(self):
        return f'{self.name} für {self.__personen} Personen. Zutaten: {self.__zutaten}'

    def print_rezept(self):
        print(self.__str__())

    def umrechnen(self, personen: int) -> "Rezept":
        faktor = personen / self.__personen
        zutaten_neu = []
        for z in self.zutaten:
            zutaten_neu.append(Zutat(z.name, z.menge * faktor))
        return Rezept(self.name, personen, zutaten_neu)

if __name__ == '__main__':
    brokkoli = Zutat("brokkoli", 1)
    penne = Zutat("penne", 200)
    sahne = Zutat("Sahne", 150)
    pasta = Rezept("Pasta", 2, [brokkoli, sahne, penne])

    p = Rezept("Vogerlsalat", 4, [Zutat("Vogerlsalat", 2), Zutat("Kernöl", 1), Zutat("Essig", 1), Zutat("Ei gekocht", 2)])
    p.print_rezept()
    p3 = p.umrechnen(2)
    p.print_rezept()
    p3.print_rezept()
    pasta.print_rezept()
