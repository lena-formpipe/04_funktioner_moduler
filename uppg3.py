# 3 Spelet 21
# Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större.
# Förr eller senare kommer man förbi 21.
# Skriv en funktion som skriver ut det första talet i talserien som är större än 21.
import random

# Version 1
def find_sum_21(initial_value:int):
    find_21 = 21
    if initial_value > find_21:
        print(f"Du har angett startvärde {initial_value} vilket är högre än {find_21} så funktionen kan inte användas.")
    elif initial_value == find_21:
        print(f"Du har angett startvärde = {initial_value} så värdet är redan givet.")
    else:
        iterations = 0
        sum = initial_value
        new_value = initial_value
        while sum < find_21:
            new_value += 1
            sum = sum + new_value
            iterations += 1

        print(f"Du angav {initial_value} som startvärde.")
        print(f"Efter {iterations} summeringar av har vi hittat det närmsta värdet över {find_21}, vilket är {sum}")
    return


# Testa version 1
print("Version 1 där man anger startsiffra manuellt:")
find_sum_21(1)


# Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
# Tips: importera modulen random och använd funktionen randint för att slumpa tal.
# Exempel: card = random.randint(1, 13)

def find_sum_21_random():
    list_of_cards = []
    find_21_random = 21
    iterations = 0
    sum = 0
    while sum < find_21_random:
            card = random.randint(1, 13)
            list_of_cards.append(card)
            sum = sum + card
            iterations += 1

    print(f"Listan av slumpade kort är {list_of_cards}.")
    print(f"Efter {iterations} slumpade kort av har vi hittat det närmsta värdet över {find_21_random}, vilket är {sum}.")
    return


# Testa version 2
print("\nVersion 2 där man slumpar startsiffra:")
find_sum_21_random()