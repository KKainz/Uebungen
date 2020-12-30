

def istSchaltjahr(jahr: int) -> bool:
    if (jahr % 400) == 0:
        return True
    elif (jahr % 100) == 0:
        return False
    elif (jahr % 4) == 0:
        return True

    return False

if __name__ == '__main__':
    print(istSchaltjahr(2018))
    print(istSchaltjahr(2020))
    