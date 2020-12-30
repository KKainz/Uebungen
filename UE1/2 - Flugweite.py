

def flugweite(weite: float) -> float:
    if weite > 198.7:
        return "Erster"
    elif weite > 197.1:
        return "Zweiter"
    elif weite > 195:
        return "Dritter"
    elif weite == 193.67:
        return "Vierter"
    elif weite > 100 and weite < 150:
        return "letzter Platz"
    elif weite > 20 and weite < 50:
        print('Call Ambulance!')
        return None
    else:
        print('Nicht in Angabe')


if __name__ == '__main__':
    print(flugweite(200))
    print(flugweite(194.4))
    print(flugweite(197.2))
    print(flugweite(30))
    print(flugweite(193.67))