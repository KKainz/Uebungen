import random

def wie_oft_wuerfeln(ziffer: int, anzahl: int) -> int:
    zaehler = 0
    gefunden = 0

    while gefunden < anzahl:
        x = random.randint(1,6)
        zaehler += 1
        if x == ziffer:
            gefunden += 1
    return zaehler


if __name__ == '__main__':
    print(wie_oft_wuerfeln(3,100))
    print(wie_oft_wuerfeln(2, 50))