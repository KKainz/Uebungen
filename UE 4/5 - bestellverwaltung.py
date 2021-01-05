from typing import List

class Bestellzeile:

    def __init__(self, name: str, menge: int, preis: int):
        self.name = name
        self.menge = menge
        self.preis = preis

    def get_kosten(self) -> float:
        return self.menge * self.preis

class Bestellung:

    def __init__(self, nummer: str, zeilen: List[Bestellzeile]):
        self.nummer = nummer
        self.zeilen = zeilen

    def print_bestellung(self):
        print(f'Bestellung Nummer {self.nummer}:')
        for z in self.zeilen:
            print(f'{z.name}: {z.menge} Stück à {z.preis} EUR')

    def get_kosten(self) -> float:
        p = 0
        for z in self.zeilen:
            p += z.get_kosten()
        return p


if __name__ == '__main__':
    a = Bestellzeile("Produkt A", 5, 10)
    b = Bestellung(1, [Bestellzeile("a", 2, 10), Bestellzeile("b", 5, 50), Bestellzeile("c", 7, 2)])


    a.get_kosten()
    b.print_bestellung()
    print(b.get_kosten())