import abc
from typing import List, Dict
import math

# 1 - Abschreibung
class Anlage:

    def __init__(self, bezeichnung: str, initialer_wert: float, nutzungsdauer: int):
        self.__bezeichnung = bezeichnung
        self.__initialer_wert = initialer_wert
        self.__nutzungsdauer = nutzungsdauer
        self.__alter = 0
        self.__restwert = initialer_wert

    @property
    def bezeichnung(self):
        return self.__bezeichnung

    @property
    def initialer_wert(self):
        return self.__initialer_wert

    @property
    def nutzungsdauer(self):
        return self.__nutzungsdauer

    def __repr__(self):
        return f'{self.__bezeichnung}: Wert = {self.__restwert}, Nutzungsdauer = {self.__nutzungsdauer}'

    def abschreiben(self):
        r = self.__restwert
        if self.__alter <= self.__nutzungsdauer:
            r = self.__initialer_wert / self.__nutzungsdauer * (self.__nutzungsdauer - self.__alter)
        else:
            r = self.__alter + 1
        return math.floor(r)

    def simuliere(self, max_jahre: int, min_wert: int):
        counter = 0
        while counter < max_jahre or self.__restwert < min_wert or self.__restwert == 0:
            counter += 1
            self.abschreiben()
        return self.__restwert

    def renew(self, zusatz_wert: int, zusatz_jahre: int) -> "Anlage":
        return Anlage(self.__bezeichnung, self.__restwert + zusatz_wert, self.__nutzungsdauer - self.__alter + zusatz_jahre)

# 2 - Bonusberechnung

class Mitarbeiterin:

    __mitarbeiter_zaehler = 1

    def __init__(self, vorname: str, nachname: float, gehalt: float, alter: int):
        self.vorname = vorname
        self.nachname = nachname
        self.__mitarbeiter_nummer = self.__mitarbeiter_zaehler
        self.__mitarbeiter_zaehler += 1
        self.gehalt = gehalt
        self.__alter = alter

    @property
    def mitarbeiter_nummer(self):
        return self.__mitarbeiter_nummer

    @property
    def alter(self):
        return self.__alter

    def monats_abrechnung(self) -> float:
        sv_abgezogen = (self.gehalt * 12) * 0.8
        g_ohne_SV = sv_abgezogen
        steuer = 0
        if g_ohne_SV > 50000:
            steuer += (g_ohne_SV - 50000) * 0.6
            g_ohne_SV = 50000
        if g_ohne_SV > 30000:
            steuer += (g_ohne_SV - 30000) * 0.45
            g_ohne_SV = 30000
        if g_ohne_SV > 20000:
            steuer += (g_ohne_SV - 20000) * 0.32
            g_ohne_SV = 20000
        if g_ohne_SV > 10000:
            steuer += (g_ohne_SV - 10000) * 0.2
            g_ohne_SV = 10000
        if g_ohne_SV <= 10000:
            steuer += g_ohne_SV * 0.1
        return (sv_abgezogen - steuer) / 12

    def jahresabrechnung(self, monate: float) -> float:
        return self.monats_abrechnung() * monate

# 3 - Verwaltungsstrafe

class StVO_Strafen:

    __strafnummer = 1

    def __init__(self, vorname: str, nachname: str, kennzeichen: str):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__kennzeichen = kennzeichen
        self.__strafnummer += 1
        self.__strafe = 0
        self.__anzahl = 0

    def __repr__(self):
        return f'{self.__vorname} {self.__nachname}: {self.__anzahl} Strafen, {self.__strafe} EUR'

    def strafe_geschwindigkeit(self, geschwindigkeitsueberschreitung: int):
        self.__anzahl += 1
        if geschwindigkeitsueberschreitung <= 20:
            self.__strafe += 30
        elif geschwindigkeitsueberschreitung <= 30:
            self.__strafe += 50
        elif geschwindigkeitsueberschreitung <= 50:
            self.__strafe += 100
        elif geschwindigkeitsueberschreitung <= 100:
            self.__strafe += 500
        else:
            self.__strafe += 1500

    def verbandspaket(self):
        self.__anzahl += 1
        self.__strafe += 25

    def alkohol(self, promille: float):
        self.__anzahl += 2
        if 0.5 <= promille < 1:
            self.__strafe += 100
        elif 1 <= promille < 2:
            self.__strafe += 400
        elif 2 <= promille < 3:
            self.__strafe += 1000
        elif promille >= 3:
            self.__strafe += 5000

    def sonstiges(self, wert: float):
        self.__anzahl += 1
        self.__strafe += wert

    @property
    def strafe(self):
        if self.__anzahl == 1:
            return self.__strafe * 0.7
        elif self.__anzahl == 2:
            return self.__strafe * 0.8
        elif self.__anzahl == 3:
            return self.__strafe * 0.9
        else:
            return self.__strafe

# 4 - Rezeptverwaltung

class Zutat:

    def __init__(self, name: str, menge: int):
        self.__name = name
        self.__menge = menge

    def __repr__(self):
        return f'{self.__menge} g/ml {self.__name}'

    @property
    def name(self):
        return self.__name

    @property
    def menge(self):
        return self.__menge

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
        return f'{self.__name} für {self.__personen} Personen, Zutaten: {self.__zutaten}'

    def print_rezept(self):
        print(self.__str__())

    def umrechnen(self, personen: int) -> "Rezept":
        faktor = personen / self.__personen
        zutaten_n = []
        for z in self.__zutaten:
            zutaten_n.append(Zutat(z.name, z.menge * faktor))
        return Rezept(self.__name, personen, zutaten_n)

# 5 - Bestellverwaltung

class Bestellzeile:

    def __init__(self, name: str, menge: int, preis: int):
        self.name = name
        self.menge = menge
        self.preis = preis

    def get_kosten(self) -> float:
        return self.menge * self.preis

    def __repr__(self):
        return f'{self.name}: {self.menge} Stück à {self.preis} EUR'

class Bestellung:

    def __init__(self, nummer: str, zeilen: List[Bestellzeile]):
        self.nummer = nummer
        self.zeilen = zeilen

    def print_bestellung(self):
        print(f'Bestellung Nr {self.nummer}: {self.zeilen}')

    def get_kosten(self) -> float:
        w = 0
        for p in self.zeilen:
            w += p.get_kosten()
        return w



if __name__ == '__main__':
    pc = Anlage("PC", 1500, 1)
    print(pc.abschreiben())
    print(pc.simuliere(5, 2))
    print(pc.renew(1000, 6))
    pc.__repr__()

    a = Mitarbeiterin("A", 10, 4000, 44)
    print(a.monats_abrechnung())
    print(a.jahresabrechnung(11.5))

    b = StVO_Strafen("Bob", "Builder", "B-1254G")
    b.strafe_geschwindigkeit(100)
    b.verbandspaket()
    b.sonstiges(45)
    print(b.__repr__())
    print(b.strafe)
    b.alkohol(1.6)
    b.sonstiges(30)
    b.strafe_geschwindigkeit(15)
    print(b.__repr__())
    print(b.strafe)

    c = Zutat("Chili", 50)
    d = Zutat("Dralli (Pasta)", 150)
    s = Zutat("Sahne", 150)
    r = Rezept("Chili-Sahne Pasta", 4, [c, d, s])
    r.print_rezept()
    print(r.umrechnen(2))

    pen = Bestellzeile("Stift", 50, 2)
    pap = Bestellzeile("Papier", 10, 3)
    usb = Bestellzeile("USB-Kabel", 3, 10)
    print(usb.get_kosten())
    best = Bestellung("A-1254", [pap, pen, usb])
    best.print_bestellung()
    print(best.get_kosten())