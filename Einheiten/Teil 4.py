

verkauf_kw = [90000, 30000, 40000, 20000, 10000]

for kw in verkauf_kw:
    print(kw)

def countdown(zahl: int):
    for z in range(zahl, -1, -1):
        print(z)

def kleine_zeichen(par: str) -> int:
    zaehler = 0
    for a in par:
        if a.islower():
            zaehler += 1
    return zaehler

def finde_kleinste_zahl(liste) -> int:
    min_idx = 0
    for z in range(1, len(liste)):
        if liste[z] < liste[min_idx]:
            min_idx = z
    return min_idx

def fizz_buzz():
    for zahl in range(1, 101):
        if (zahl % 3) == 0 and (zahl % 5) == 0:
            print("FizzBuzz")
        elif (zahl % 3) == 0:
            print("Fizz")
        elif (zahl % 5) == 0:
            print("Buzz")
        else:
            print(zahl)

if __name__ == '__main__':
    print(kw)
    countdown(10)
    print(kleine_zeichen("haLLo sweEtIE"))
    print(finde_kleinste_zahl([1, 8, 65, 10804, 4, 0.5]))
    fizz_buzz()