import random

def ratespiel() -> float:
    erg = random.randint(1,100)
    guess = -1
    versuche = 0
    print("Errate meine Zahl!")
    while erg != guess:
        guess = int(input())
        versuche += 1

        if guess < erg:
            print("Etwas höher...")
        elif guess > erg:
            print("Etwas niedriger...")

    print(f'Richtig geraten nach {versuche} Versuchen')

if __name__ == '__main__':
    ratespiel()