
class Strafen:

    __strafzaehler = 1

    def __init__(self, vorname: str, nachname: str, kennzeichen: str):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__kennzeichen = kennzeichen
        self.__strafnummer = Strafen.__strafzaehler
        Strafen.__strafzaehler += 1

        self.__strafe = 0.0
        self.__anzahl = 0

        @property
        def vorname(self):
            return self.__vorname

        @property
        def nachname(self):
            return self.__nachname

        @property
        def kennzeichen(self):
            return self.__kennzeichen
        
        @property
        def strafnummer(self):
            return self.__strafnummer

    @property
    def strafe(self):
        if self.__anzahl == 1:
            rabatt = 0.3
        elif self.__anzahl == 2:
            rabatt = 0.2
        elif self.__anzahl == 3:
            rabatt = 0.1
        else:
            rabatt = 0
        return self.__strafe * (1 - rabatt)

    def raserstrafe(self, geschwindigkeitsueberschreitung: int) -> int:
        self.__anzahl += 1
        if geschwindigkeitsueberschreitung <= 20:
            self.__strafe += 30
        elif geschwindigkeitsueberschreitung <= 30:
            self.__strafe += 50
        elif geschwindigkeitsueberschreitung <= 50:
            self.__strafe += 100
        elif geschwindigkeitsueberschreitung <= 100:
            self.__strafe += 500
        elif geschwindigkeitsueberschreitung > 100:
            self.__strafe += 1500

    def verbandspaket(self):
        self.__anzahl += 1
        self.__strafe += 25

    def alkohol(self, promille: float):
        self.__anzahl += 2
        if promille >= 0.5 and promille <1:
            self.__strafe += 100
        elif promille >= 1 and promille < 2:
            self.__strafe += 400
        elif promille >= 2 and promille < 3:
            self.__strafe += 1000
        elif promille >= 3:
            self.__strafe += 5000


if __name__ == '__main__':
    a = Strafen("Max", "Mustermann", "G 4324")
    a.alkohol(1.2)
    a.raserstrafe(56)
    a.verbandspaket()
    print(a.strafe)
