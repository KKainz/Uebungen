

def wieweitSpazieren(gewicht: float, letzesMal: float, vertraegtsich: bool) -> float:
    if gewicht < 5:
        if not vertraegtsich:
            return "2 km"
        else:
            return  "4 km"
    elif gewicht > 15 or letzesMal > 24:
        while vertraegtsich:
            return "8 km"
    else:
        return "5 km"

if __name__ == '__main__':
    print(wieweitSpazieren(0.8, 15, False))
    print(wieweitSpazieren(10, 2, False))
    print(wieweitSpazieren(3.5, 8, True))
    print(wieweitSpazieren(20, 26, True))
    print(wieweitSpazieren(20, 26, False))