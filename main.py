# 2 MAIN
# Öva på funktioner och moduler
# Samla ihop dina funktioner så att de ligger i en eller flera moduler.
# Importera och anropa dem från main.py,
# så att main-filen bara innehåller funktionsanrop.

from uppg2_funktioner_moduler import my_function, eko, eko_count, last, cut_edges, increase, average, pretty_print

# 1
print("\nUppgift 1")
my_function("Lena")

# 2a
print("\nUppgift 2a")
eko("Lena")

# 2b
print("\nUppgift 2b")
eko_count("Lena", 3)

print("\nUppgift 3")
lista1 = ["hej", "då", "alla", "barn"]

print("\nUppgift 4")
print(last(lista1))

print("\nUppgift 5")
print(cut_edges(lista1))

print("\nUppgift 6")
print(increase(1))

print("\nUppgift 7")
print(average(10, 20))

print("\nUppgift 8")
pretty_print(["a", "b", 3.14])
pretty_print([])