
class Mitarbeiterin:

    __mitarbeiterzaehler = 1

    def __init__(self, vorname: str, nachname: str, bruttogehalt: float, alter: int):
        self.vorname = vorname
        self.nachname = nachname
        self.bruttogehalt = bruttogehalt
        self.__alter = alter
        self.__mitarbeiternummer = self.__mitarbeiterzaehler
        self.__mitarbeiterzaehler += 1

    @property
    def alter(self):
        return self.__alter

    @property
    def mitarbeiternummer(self):
        return self.__mitarbeiternummer

    def monats_abrechnung(self, monate = 12) -> float:
        sv_abgezogen = (self.bruttogehalt * 12) * 0.8
        zu_versteuern = sv_abgezogen
        steuer = 0
        if zu_versteuern > 50000:
            steuer += (zu_versteuern - 50000) * 0.6
            zu_versteuern = 50000
        if zu_versteuern > 30000:
            steuer += (zu_versteuern - 30000) * 0.45
            zu_versteuern = 30000
        if zu_versteuern > 20000:
            steuer += (zu_versteuern - 20000) * 0.32
            zu_versteuern = 20000
        if zu_versteuern > 10000:
            steuer += (zu_versteuern - 10000) * 0.2
            zu_versteuern = 10000
        steuer += zu_versteuern * 0.1
        return (sv_abgezogen - steuer) / monate

    def jahres_abrechnung(self, monate = 12) -> float:
        return self.monats_abrechnung(monate) * monate

if __name__ == '__main__':
    m = Mitarbeiterin("Max", "Mustermann", 3300, 35)
    print(m.monats_abrechnung())
    print(m.jahres_abrechnung(9))
