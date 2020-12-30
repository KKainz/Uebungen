

def geld_verzinsen(betrag: float, zeit: int, prozent: float) -> float:
    erg = betrag
    for z in range(zeit):
        erg = (erg * (prozent / 100)) * zeit
    return erg

def kontostandPLUSzinsen(betrag2: float, zeit2: int, zinsen2: float) -> float:
    erg2 = betrag2
    for z in range(zeit2):
        erg2 = erg2 + (erg2 * (1 + zinsen2 / 100))
    return erg2

if __name__ == '__main__':
    print(geld_verzinsen(5000, 2, 2))
    print(kontostandPLUSzinsen(5000, 2, 2))