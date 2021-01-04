from typing import List, Dict, Tuple, Set, Any

class Anlage:

    def __init__(self, bezeichnung: str, initialer_wert: float, nutzungsdauer: int, rest_wert: float, alter: int):
        self.bezeichnung = bezeichnung
        self.initialer_wert = initialer_wert
        self.nutzungsdauer = nutzungsdauer
        self.rest_wert = initialer_wert
        self.alter = 0

    @property
    def bezeichung(self):
        return self.__bezeichnung

    @property
    def initialer_wert(self):
        return self.__initialer_wert

    @property
    def nutzungsdauer(self):
        return self.__nutzungsdauer

    @property
    def rest_wert(self):
        return self.__rest_wert

    @property
    def alter(self):
        return self.__alter

    def abschreiben(self):
        self.__alter += 1









if __name__ == '__main__':
    pass