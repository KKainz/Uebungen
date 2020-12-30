

def reihe() -> float:
    erg = 0
    for x in range(2, 101):
        erg += 1 / x
    return erg

if __name__ == '__main__':
    print(reihe())