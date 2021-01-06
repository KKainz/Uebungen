from typing import List, Dict
import abc

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

    def __init__(self, name: str, gewicht: int, gewicht_federn: int):
        super().__init__(name, gewicht)
        self.gewicht_federn = gewicht_federn

    def get_full_weight(self) -> int:
        g1 = self._gewicht + self.gewicht_federn
        return g1

    def make_noise(self) -> str:
        return f'Quack quack'

    def __repr__(self):
        return f'Flugente {self._name}'

class BadeEnte(Ente):

    def __init__(self, name: str, gewicht: int, gewicht_wasser: int):
        super().__init__(name, gewicht)
        self.gewicht_wasser = gewicht_wasser

    def __repr__(self):
        return f'Badeente {self._name}'

    def get_full_weight(self) -> int:
        g2 = self._gewicht + self.gewicht_wasser
        return g2

    def make_noise(self) -> str:
        return f'Quackiii'

class Entenhausen:
    def __init__(self):
        self.__liste_enten = []

    def addEnte(self, e: Ente):
        self.__liste_enten.append(e)

    def get_gruppierte_enten(self) -> Dict[int, List[Ente]]:
        aufteilung = {100: [], 200: [], 300: []}
        for e in self.__liste_enten:
            w = e.get_full_weight()
            if w <= 100:
                aufteilung.get(100).append(e)
            elif w > 100 and w <= 200:
                aufteilung.get(200).append(e)
            elif w > 200 and w <= 300:
                aufteilung.get(300).append(e)
        return aufteilung




if __name__ == '__main__':

    b = FlugEnte("Berta", 10, 1)
    print(b.__repr__())
    print(b.get_full_weight())
    c = BadeEnte("Donald", 250, 2)
    print(c.get_full_weight())
    print(c.__repr__())
    eh = Entenhausen()
    eh.addEnte(FlugEnte("Trick", 50, 20))
    eh.addEnte(b)
    eh.addEnte(c)
    print(eh.get_gruppierte_enten())