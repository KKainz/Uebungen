

def lohnsteuer(gehalt: float) -> float:
    steuer = 0
    rest_gehalt = gehalt
    if rest_gehalt > 1000000:
        steuer += (rest_gehalt - 1000000) * 0.55
        rest_gehalt = 90000
    if rest_gehalt > 90000:
        steuer += (rest_gehalt - 90000) * 0.5
        rest_gehalt = 60000
    if rest_gehalt > 60000:
        steuer += (rest_gehalt - 60000) * 0.48
        rest_gehalt = 31000
    if rest_gehalt > 31000:
        steuer += (rest_gehalt - 31000) * 0.42
        rest_gehalt = 25000
    if rest_gehalt > 25000:
        steuer += (rest_gehalt - 25000) * 0.35
        rest_gehalt = 25000
    if rest_gehalt > 18000:
        steuer += (rest_gehalt - 18000) * 0.35
        rest_gehalt = 18000
    if rest_gehalt > 11000:
        steuer += (rest_gehalt - 11000) * 0.2

    return steuer

def jahresLohnsteuerAbzug(einkommen: float) -> float:
    Stufen = [[1000000, 0.55], [90000, 0.5], [60000, 0.48], [31000, 0.42], [18000, 0.35], [11000, 0.2]]
    steuer = 0
    resteinkommen = einkommen

    for tar in Stufen:
        if resteinkommen > tar[0]:
            steuer += (resteinkommen - tar[0]) * tar[1]
            resteinkommen = tar[0]

    return steuer


if __name__ == '__main__':
    print(lohnsteuer(45000))
    print(lohnsteuer(18001))
    print(jahresLohnsteuerAbzug(42000))
    print(jahresLohnsteuerAbzug(954781))
    print(jahresLohnsteuerAbzug(18001))