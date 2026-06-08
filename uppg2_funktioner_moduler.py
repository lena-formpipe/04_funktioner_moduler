# 2 Öva på funktioner och moduler
# Samla ihop dina funktioner så att de ligger i en eller flera moduler.
# Importera och anropa dem från main.py,
# så att main-filen bara innehåller funktionsanrop.

# 1
# Skriv en funktion som tar en sträng som parameter.
# Vid anrop skrivs ut strängen och "är en fena på programmering".
def my_function(name):
    print(f"{name} är en fena på programmering!")

# 2a Skriv en funktion med namnet "eko".
# När den anropas med en sträng ska den upprepa strängen,
# och skriva ut resultatet.
def eko(param):
    print(f"{param} {param}")

# 2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas.
# Exempel: eko("hej", 3) → skriver ut "hejhejhej"
def eko_count(param, count:int):
    string_to_print = ""
    for y in range(count):
        string_to_print = string_to_print + param
    print(string_to_print)

# 3 Följande kod ska sluta loopa efter 5 varv.
# Flytta den in i en funktion och justera den enligt kommentaren.
# end = 5
# y = 1
# for x in range(1, 100):
#    y *= 2
#    # avsluta loopen med en if-sats här
#    print("HJÄLP GÖR KLART")
# print(y)

# 4 Skriv en funktion med namnet last.
# Den ska ta en lista som parameter och returnera det sista elementet i listan.
# last([1, 2, 3]) → 3
def last(lista):
    return lista[-1]

# 5 Skriv en funktion med namnet cut_edges.
# Den ska ta en lista som parameter.
# När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
# cut_edges([1, 2, 3, 4]) → [2, 3]
def cut_edges(lista):
    lista.pop(0)
    lista.pop(-1)
    return lista

# 6 Lös felen i koden.
def increase(x):
    x += 1
    return x


# 7 Bygg en funktion med namnet average.
# Den ska ta parametrar: x och y. Båda ska vara tal.
# Funktionen ska returnera medelvärdet.
# Ex medelvärdet av 4 och 8: (4 + 8) / 2, vilket blir 6.
def average(x:int, y:int):
    genomsnitt = (x + y)/2
    return genomsnitt


# 8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
# Först ska funktionen tala om ifall listan är tom, eller hur många element den har.
# Sedan ska funktionen skriva ut elementen i en punktlista.
# Exempel: # pretty_print(["a", "b", 3.14])
# Listan har 3 element:
# 1. a
# 2. b
# 3. 3.14
def pretty_print(lista):
    if len(lista) == 0:
        print("listan är ju tom!")
    elif len(lista) > 0:
        length = len(lista)
        print(f"Listan har {length} element:")
        for x in range(length):
            y = x + 1
            print(f"{y}. {lista[x]}")
    return



