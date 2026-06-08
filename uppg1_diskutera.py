# 1 Läsa och förstå kod - diskutera i grupp
# Skriv ner vad du tror kommer skrivas ut.
# Skriv sedan in koden i din IDE, exakt som den står, och kör den.
# Fick du samma resultat som du trodde? Om inte, varför?

# 1a
print("1a")
print("Funktionen skriver alltid ut Test eftersom parametern inte används i funktionen.")

def foo(t):
    print("test")

foo("hej")

# 1b
print("\n1b")
print("exemplet skriver INTE ut funktionen för man har bara angett en print och inte anropat funktionen ")
def fun1(x, y):
    return x * y

print(3, 5)
print("Om man anropar funktionen korrekt så skrivs produkten av parametrarna ut:")
print(fun1(3, 5))

# 1c är korrekt anrop om 1b
print("\n1c")
print("1c är korrekt anrop av funktionen fun1")
print(fun1(3, 5))

# 1d
# 5 * (5*2 + 5*3) = 5 * 25 = 125
print("\n1d skriver ut 125")
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

# 1e funktionen lägger till värde +1 till parametern
# MEN funktionen anropas aldrig!
# a = a + 2 = 7
print("\n1e skriver ut 7 för funktionen fun3 anropas aldrig")
a = 5
def fun3(a):
    a += 1

a += 2
print(a)

# 1f
# fattar inte riktigt denna
print("\n1f anropar inte foo(param) korrekt eftersom ingen parameter skickas med?")
print("förstår inte denna övning hur det kan bli 18....")

def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)
print("ovan är utskrivet a från övning 1f.\n")

# 1g Funktionen "isinstance" kan kontrollera en variabels datatyp.
# Vad gör funktionen is_number?
# --> funktionen SKA returnerar True om parametern det är int eller float
# Går det att förbättra koden?)
# --> TO-DO -
# OM JAG Anger FALSE vilket jag inte kan förstå...??
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

b="b"
print(is_number(5.5))
print(is_number(42))
print(is_number(False))

# 1h
# Vad funktionen gör:
# om LÄNGDEN på item i ett index för parametern strings är högre än 4, mindre än 8
# så lägg till item i listan found
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found
average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
# Mitt tillägg för att se svaret utskrivet
print("\növning 1h")
print(average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"]))

# 1i
# En uppgift i tre delar:
# 1. Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
#       Svar: att hitta lägsta numret i en lista
# 2. Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
#       Svar: -11, 0, 0
# 3. Rätta felen, så funktionen gör det den ska.
#       Svar: måste justera för tom lista
#       och funktionen enbart tar värden som FINNS i listan (inte default utgår från 0)

print("\n1i")
def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])
print("slut test 1i")


