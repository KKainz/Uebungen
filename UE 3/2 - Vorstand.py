from typing import Dict, List, Tuple, Set, Any

def berechnung_Vorstand(daten: List[Tuple[str, float]]) -> Dict[str, List[Any]]:
    """ Erstellt eine Aufschlüsselung des Umsatzes in Preisregionen als Dictionary

    Parameter:
    ------
    daten: list of tuple of str, float
        Daten aus Verkaufssystem, pro Verkauf: Gerätename + Preis
    :returns
    -----
    dict of str, list of str, float, float
        Datenstruktur für Visualisierungssytem
        Bsp: {"günstig": [1, 200, 200], "normal": [3, 750, 250], "premium": [2, 2000, 1000]}
    """
    l_guenstig = [0, 0, 0]
    l_normal = [0, 0, 0]
    l_premium = [0, 0, 0]
    for tl in daten:
        if tl[1] < 300:
            l_guenstig[0] += 1
            l_guenstig[1] += tl[1]
        elif tl[1] < 600:
            l_normal[0] += 1
            l_normal[1] += tl[1]
        else:
            l_premium[0] += 1
            l_premium[1] += tl[1]
    l_guenstig[2] = l_guenstig[1] / l_guenstig[0]
    l_normal[2] = l_normal[1] / l_normal[0]
    l_premium[2] = l_premium[1] / l_premium[0]
    return {"günstig": l_guenstig, "normal": l_normal, "premium": l_premium}




l1 = [("iphone xs", 765.5), ("one plus 2", 299.99), ("iphone 12 pro", 1250), ("huawei 3", 500), ("samsung s11", 1340)]

if __name__ == '__main__':
    print(berechnung_Vorstand(l1))