# UE 1
def ist_winterreifen_pflicht(temperatur: float, schnee_fahrbahn: bool) -> bool:
    if(schnee_fahrbahn and temperatur < 6) or (temperatur <= 0):
        return True
    return False

print(ist_winterreifen_pflicht(5.9, True))

# UE 2

def geschwindigkeit(gang: int) -> float:
    if gang == 1:
        geschwindigkeit = 10
    elif gang == 2:
        gschwindigkeit = 20
    elif gang == 3:
        geschwindigkeit = 30
    elif gang == 4:
        geschwindigkeit = 40
    return geschwindigkeit

print(geschwindigkeit(3))

def geschwindigkeit_b(gang: int, wind: bool) -> float:
    if gang == 1:
        geschwindigkeit = 10
        if wind:
            geschwindigkeit *= 0.9
    elif gang == 2:
        gschwindigkeit = 20
        if wind:
            geschwindigkeit *= 0.8
    elif gang == 3:
        geschwindigkeit = 30
        if wind:
            geschwindigkeit *= 0.6
    elif gang == 4:
        geschwindigkeit = 40
        if wind:
            geschwindigkeit *= 0.6
    return geschwindigkeit

print(geschwindigkeit_b(3,True))

def geschwindigkeit_c(gang: int, wind: bool, windrichtung: bool) -> float:
    if gang == 1:
        geschwindigkeit = 10
        if wind and windrichtung:
            geschwindigkeit *= 0.9
    elif gang == 2:
        gschwindigkeit = 20
        if wind and windrichtung:
            geschwindigkeit *= 0.8
    elif gang == 3:
        geschwindigkeit = 30
        if wind and windrichtung:
            geschwindigkeit *= 0.6
    elif gang == 4:
        geschwindigkeit = 40
        if wind and windrichtung:
            geschwindigkeit *= 0.6
    return geschwindigkeit

print(geschwindigkeit_c(4, True, True))
print(geschwindigkeit_c(4, True, False))

# UE 3

def kuschel_bedarf(kuschel1: int, kuschel2: int, kuschel3: int) -> bool:
    if (kuschel1 + kuschel2 + kuschel3) > 60:
        return False
    if kuschel1 < kuschel2 and kuschel2 < kuschel3:
        return True
    if kuschel2 < 25:
        return False
    return True

print(kuschel_bedarf(5, 6, 7))
