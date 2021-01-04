from typing import Dict, List, Tuple, Set

def duplikate(liste: List[List[int]]) -> List[bool]:
    dup = []
    for i in range(len(liste)):
        teilliste = set(liste[i])
        if len(liste[i]) == len(teilliste):
            dup.append(False)
        else:
            dup.append(True)
    return dup



l1 = [[1, 2, 3], [2, 4, 2], [6, 6, 6, 9]]

if __name__ == '__main__':
    print(duplikate(l1))