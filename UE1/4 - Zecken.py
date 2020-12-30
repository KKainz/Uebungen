

def naechsteZeckenImpfung(alter: int, letztesImpfungsJahr: int, ersteAuffrischung: bool) -> int:
    if ersteAuffrischung or alter >= 60:
        return "Nächste Auffrischung: " + str(letztesImpfungsJahr + 3)
    else:
        return "Nächste Auffrischung: " + str(letztesImpfungsJahr + 8)



if __name__ == '__main__':
    print(naechsteZeckenImpfung(33, 2020, False))
    print(naechsteZeckenImpfung(65, 2018, False))
    print(naechsteZeckenImpfung(5, 2017, True))