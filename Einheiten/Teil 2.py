# UE 1

def countdown(zahl: int) -> int:
    while zahl >= 0:
        print(zahl)
        zahl -= 1

x = 10
countdown(x)

# UE 2

def runter_wuerfeln(wert: int) -> int:
    print("Start " + str(wert))
    while wert > 0:
        eingabe = int(input())
        if eingabe >= 1 and eingabe <= 6:
            wert -= eingabe
            print(wert)
    print("Gewonnen!")

# runter_wuerfeln(50)

def runter_wuerfeln_b(wert: int) -> int:
    print("Start " + str(wert))
    zaehler = 0
    while wert > 0:
        eingabe = int(input())
        if eingabe >= 1 and eingabe <= 6:
            wert -= eingabe
            zaehler += 1
            print(wert)
    print("Gewonnen!")
    return zaehler

# print(runter_wuerfeln_b(33))

def runter_wuerfeln_c(wert: int) -> int:
    print("Start " + str(wert))
    zaehler = 0
    while wert != 0:
        eingabe = int(input())
        if eingabe >= 1 and eingabe <= 6:
            if (wert - eingabe) < 0:
                wert += eingabe
            else:
                wert -= eingabe
            zaehler += 1
            print(wert)
    print("Gewonnen!")
    return zaehler

# print(runter_wuerfeln_c(14))

# UE 3

def fibonacci(grenzwert: int) -> int:
    z1 = 0
    z2 = 1
    print(z1)
    print(z2)

    while ((z1 + z2) <= grenzwert):
        erg = z1 + z2
        print(erg)

        z1 = z2
        z2 = erg

print(fibonacci(100))
