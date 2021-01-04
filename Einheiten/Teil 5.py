from typing import Dict, List, Set, Tuple
import random

l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def hauptdiagonale(liste : List[List[int]]) -> int:
    sum = 0
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if i == j:
                sum += liste [i] [j]
    return sum

def hauptdiagonale2(liste : List[List[int]]) -> int:
    sum = 0
    for i in range(len(liste)):
        sum += liste [i] [i]
    return sum

def verkaufte_smartphones(geraete: List[str]) -> Dict[str, int]:
    erg = {}
    for g in geraete:
        erg[g] = erg.get(g, 0) + 1
    return erg

verkauft = ["iphone 11", "iphone 12", "iphone 11", "iphone 12", "iphone 12 pro", "iphone 11", "pixel 4", "pixel 4"]

l2 = [[1, 2, 3],[5, 6, 7],[10, 15, 20],[1000, 2000]]

def mittelwerte(zahlen: List[List[float]]) -> float:
    avg = []
    for i in range(len(zahlen)):
        sum = 0
        for j in range(len(zahlen[i])):
            sum += zahlen [i] [j]
        avg.append(sum / len(zahlen[i]))
    return avg

l3 = ["A", "B", "C", "D", "E"]
l4 = ["C", "D", "E", "F"]
l5 = ["F", "A"]

def lucky_looser(looser1 : List[str], looser2: List[str], nr_winner: int) -> List[str]:
    potential = list(set(looser1).intersection(set(looser2)))
    winners = []
    for nr in range(nr_winner):
        if len(potential) == 0:
            break
        w = random.choice(potential)
        winners.append(w)
        potential.remove(w)
    return f'Lucky Looser: {nr_winner}, Namen: {winners}'



if __name__ == '__main__':
    print(hauptdiagonale(l))
    print(hauptdiagonale2(l))
    print(verkaufte_smartphones(verkauft))
    print(mittelwerte(l2))
    print(lucky_looser(l3, l4, 3))
