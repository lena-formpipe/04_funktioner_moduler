# Uppgift 4 Pokerhand
# INTE HELT KLAR UPPGIFT
# # Du ska bygga en funktion som kan utvärdera en pokerhand (5 kort) och tala om hur bra den är.
# Exempel på körning: poker_hand(cards) --> "Du fick ett par med valören: 5"
import random

# 1 Bygg en funktion som slumpar ETT spelkort.
# Den ska returnera en lista med två element: färg och valör.
# Färg kan vara: ruter, hjärter, spader eller klöver.
# Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
# Exempel på ett kort: ["hjärter", 12]

def random_poker_card():
    poker_card =[]
    # random.randint(a, b) genererar ett slumptal mellan a och b
    # det finns fyra färger som representeras av 1 till 4,
    # där varje heltal översätts till en färg enligt if-satsen nedan
    poker_card_color = random.randint(1, 4)
    if poker_card_color == 1:
        color = "hjärter"
    elif poker_card_color == 2:
        color = "spader"
    elif poker_card_color == 3:
        color = "ruter"
    elif poker_card_color == 4:
        color = "klöver"
    # random.randint(a, b) genererar ett slumptal mellan valörerna 2 och 14
    # vilket motsvarar korten 2 till ess (=14)
    value = random.randint(2, 14)
    # Lägger till dessa så att färgen kommer först och sedan valören
    poker_card.append(color)
    poker_card.append(value)
    return poker_card


print("Uppgift 1 skriv ut ett slumpat pokerkort:")
new_card = random_poker_card()
print(new_card)


# 2 Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.
# extended: Jag kollar även om vilket kort som är större eller mindre och skriver ut detta.

def compare_card_value_extended(first_card:[], second_card:[]):
    # jag skriver ut korten för att kunna bedöma om funktionen gör rätt
    print(f"Kort1 är {first_card}")
    print(f"Kort2 är {second_card}")
    # valören finns i index == 1
    color = 0
    value = 1
    if first_card[value] == second_card[value]:
        print(f"Korten är av samma valör: ({first_card[value]}).\n")
        return True
    elif first_card[value] < second_card[value]:
        print(f"Kort1 ({(first_card[value])}) är av lägre valör än Kort2 ({second_card[value]}).\n")
        return False
    elif first_card[value] > second_card[value]:
        print(f"Kort1 ({first_card[value]}) är av högre valör än Kort2 ({second_card[value]}).\n")
        return False


print("\nTest av version 2_extended, som både jämför om valören är lika eller vilken som är störst:")
poker_card1 = random_poker_card()
poker_card2 = random_poker_card()
compare_card_value_extended(poker_card1, poker_card2)


# 2 kontrollerar om kort har samma valör, om så är fallet returneras true (annars false)

def is_same_value(first_card:[], second_card:[]):
    # valören finns i index == 1
    value = 1
    if first_card[value] == second_card[value]:
        return True
    else:
        return False


# 2 kontrollerar om kort har samma färg, om så är fallet returneras true (annars false)
def is_same_color(first_card:[], second_card:[]):
    # färgen finns i index = 0
    color = 0
    if first_card[color] == second_card[color]:
        return True
    else:
        return False


print("\nUppgift 2: Test av is_same_value and is_same_color:")
poker_card_a = random_poker_card()
poker_card_b = random_poker_card()
print(poker_card_a)
print(poker_card_b)
same_value = is_same_value(poker_card_a, poker_card_b)
same_color = is_same_color(poker_card_a, poker_card_b)
print(f"Same value: {same_value}")
print(f"Same color: {same_color}")


# Uppgift 3: slumpa FEM kort i en pokerhand
def give_five_cards():
    five_cards = []
    # Fortsätt slumpa kort tills dess listan innehåller alla fem kort
    while len(five_cards) < 5:
        card = random_poker_card()
        print(card)
        # initialt gjorde jag en väldigt komplex lösning där jag först lade till i listan
        # och sedan tog bort med pop om det blev en dublett.
        # Efter lite googling så hittade jag att det finns en färdig hjälp att leta i en lista och jämföra
        # Lösningen blev då att FÖRST jämföra och om det INTE är en dublett så läggs den till i listan.
        if card not in five_cards:
            five_cards.append(card)
            print("Lägger till kortet.")
        elif card in five_cards:
            print("Oj, det slumpade kortet fanns redan i listan, jag slumpar ett nytt.")
    # För att sortera en lista baserat på det andra elementet av varje inre element
    # kan jag använda Pythons inbyggda funktion sorted() och anfe en lambda-funktion i key-argumentet
    # Detta eftersom valören kommer efter färgen i min lista.
    # jag väljer också att sortera med högsta och neråt
    five_cards = sorted(five_cards, key=lambda x: x[1], reverse=True)
    return five_cards

print("\nTest att slumpa fem spelkort.")
five_cards = give_five_cards()
print(f"Detta blev de fem korten.{five_cards}.\n")

# 3 Bygg första versionen av poker_hand(cards).
# Med hjälp av de andra funktionerna ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.
# compare_card_value(poker_card1, poker_card2)

# Denna är INTE KLAR
def check_poker_hand(hand):
    # parameter in är en pokerhand med fem kort
    # med hjälp av tuple loopar igenom varje kort i handen skapar en lista med alla fem VÄRDEN.
    # En tuple är en inbyggd datatyp i Python som används för att lagra flera objekt i en enda variabel.
    # den fungerar som en vanlig lista med är oföränderlig (immutable), kan inte ändra element efter att den skapats.
    value_list = tuple(kort[1] for kort in hand)
    value_list = sorted(value_list, reverse=True)
    print("\nfunktionen check_poker_hand skriver ut sorterad value_list av värden och färger.")
    print(value_list)

    # loopar igenom varje kort i handen och skapar en lista med alla kortens FÄRGER
    color_list = tuple(kort[0] for kort in hand)
    color_list = sorted(color_list)
    print(color_list)

    # Räkna förekomster med count()
    # set(value_list)  Tar bort alla dubbletter och ger unika värden
    # for v in set(value_list) -->  Loopar igenom varje unikt värde
    # value_list.count(v)    Räknar hur många gånger just det värdet finns i den ursprungliga tupeln
    # {v: value_list.count(v) for v in...} --> sätter ihop allt till en dictionary i Pyhton
    counts_of_a_value = {v: value_list.count(v) for v in set(value_list)}
    counts_of_a_value= sorted(counts_of_a_value, reverse=True)
    counts = sorted(counts_of_a_value.values())  # t.ex. [3, 1, 1]
    print("skriv ut dictionary:")
    print(counts_of_a_value)
    for nyckel, value in counts_of_a_value:
        print(f"{nyckel}: {value} ")
    # om längden på listan över olika färger == 1 så är alla korten i samma färg = flush
    flush = len(set(color_list)) == 1   # Alla samma färg

    # Enkel stege-kontroll (utan ess som lågt)
    value_index = sorted(value_list.index(v) for v in value_list)
    # vid en stege är differensen mellan sista kortet [-1] och första kortet[0] alltid exakt 4
    # DESSUTOM måste varje värde vara olika = längden för värden måste vara lika med 5
    stege = (value_list[-1] - value_list[0] == 4) and len(set(value_list)) == 5

    # Bedömning
    if stege and flush:
        return "Straight flush"
    elif counts[0] == 4:
        return "Fyra lika det blir fyrtal"
    elif counts == [3, 2]:
        return "Du har Kåk"
    elif flush:
        return "Du har Flush"
    elif stege:
        return "Du har Stege"
    elif counts[0] == 3:
        return "Tre lika det blir Triss"
    elif counts[:2] == [2, 2]:
        return "Två par"
    elif counts[0] == 2:
        return "Ett par"
    else:
        return "Högt kort, dvs du har en skithand"

# --- Kör ett exempel ---
hand = give_five_cards()
print("Din hand med den nya koden:")
for kort in hand:
    print(f"  {kort[0]}{kort[1]}")

svaret = check_poker_hand(hand)
print(f"\nResultat: {svaret}")
print("Hej")


# Fortsätt att lägga till fler kontroller till funktionen.
# Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
# pretty_print_card(["hjärter", 5]) → "hjärter fem"


# Lista med pokerhänder.
# ●	Ett par (två lika kort)
# ●	Två par
# ●	Tretal (tre lika)
# ●	Straight (5 kort i följd, t.ex. 7-8-9-10-11)
# ●	Flush / färg (alla kort har samma färg)
# ●	Hus (par och tretal med olika valörer)
# ●	Fyrtal
# ●	Straight flush (5 kort i följd, med samma färg)
# ●	Femtal