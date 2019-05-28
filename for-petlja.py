# for petlja

import random

tajnibroj = random.randint(1,30)

for x in range(5):

    pogodi = int(input("Pogodi jedan broj između 1 i 30: "))

    print(x)

    if tajnibroj == pogodi:
        print("Bravo pogodio si! To je bio broj ", tajnibroj)
        break
    else:
        print("Fulao si, pokušaj ponovno...")

print("Kraj programa")