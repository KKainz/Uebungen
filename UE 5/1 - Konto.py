

class Konto:

    def __init__(self, inhaber: str):
        self._inhaber = inhaber
        self._kontostand = 0

    @property
    def inhaber(self):
        return self._inhaber

    @property
    def kontostand(self):
        return self._kontostand

    def einzahlen(self, wert: float) -> float:
        if wert > 0:
            self._kontostand += wert

    def auszahlen(self, wert: float) -> float:
        if wert > 0:
            self._kontostand -= wert
        return wert

    def __repr__(self):
        return f'Kontostand {self._inhaber}: {self._kontostand}'


class Sparkonto(Konto):

    def auszahlen(self, wert: float) -> float:
        if wert < 0:
            return 0
        if wert >= self._kontostand:
            self._kontostand = 0
            w = wert
            return w
        self._kontostand -= wert
        return wert


class Girokonto(Konto):

    def __init__(self, inhaber: str, limit: float):
        super().__init__(inhaber)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def auszahlen(self, wert: float) -> float:
        if wert > 0:
            if self._kontostand > 0:
                p = self._kontostand - wert
                if p > self._limit:
                    return f'Limit erreicht, Abbuchung nicht möglich'
        return wert










if __name__ == '__main__':
    a = Konto("Andi")
    a.einzahlen(1500)
    a.auszahlen(1600)
    print(a.__repr__())

    b = Sparkonto("Berta")
    print(b.auszahlen(2))
    print(b.__repr__())

    c = Girokonto("Carsten", 500)
    c.auszahlen(499)
    print(c.__str__())

