# while petlja

import random

tajnibroj = random.randint(1,30)

while True:

    pogodi = int(input("Pogodi jedan broj između 1 i 30: "))

    if tajnibroj == pogodi:
        print("Bravo pogodio si! To je bio broj ", tajnibroj)
        break
    else:
        print("Fulao si, pokušaj ponovno...")

print("Kraj programa")