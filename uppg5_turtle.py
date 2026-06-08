# 5 Turtle graphics
# Python har ett paket med inbyggda, enkla funktioner för grafik: turtle. Tänk dig att du har en robotarm som håller en penna mot ett papper. Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:
# ●	forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
# ●	backward - gå bakåt
# ●	left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
# ●	dot - sätt ut en prick med en viss storlek
# ●	speed - normal=6, fast=10, maximal=0

import turtle as t
import math

# 1 Skriv en funktion som ritar en kvadrat.
# Längden på sidan ska vara en parameter till funktionen.
def square(sida):
    for x in range(4):
        t.forward(sida)
        t.left(90)


sida = int(input("Jag kan rita en kvadrat, ange längden på sidan: "))
square(sida)


# 2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita.
# Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater.
# Exempel:
# for x in range(5):
#     t.square()
#     t.move_next()

def move_next(distance):
    t.penup()
    t.forward(distance)
    t.pendown()

for x in range(5):
    square(5)
    move_next(10)


# 3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel.
# Använd parametrar i stället för värdena 7, 40 och 30.

def draw_cirkel(forward:int, right_angle:int):
    # om det ska bli en cirkel måste summan av vinklarna bli 360
    # antalet streck = antalet vinklar som ska ritas ut för att uppnå 360 grader
    # BERÄKNA därför range utifrån input vinkel och storlek på streck
    range_circle = int(360/right_angle)
    omkrets_cirkel = forward * range_circle
    radie = omkrets_cirkel/(2*math.pi)
    t.penup()
    # vet inte varför pennan inte positionerar sig i mitten i x-led per automatik
    # därför -50, samt att jag flyttar pennan utefter radien i y led så att cirkeln ska rymmas
    t.goto(-50, radie)
    t.pendown()

    for x in range(range_circle):
        t.forward(forward)
        t.right(right_angle)

draw_cirkel(50, 20)

# Låt de ritade bilderna ligga kvar
t. mainloop()


# 4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen.
# Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.
# INTE KLART!!

height = 20
width = 20/2

def print_p(size):
    t.goto(0,0)
    for x in range(3):
        t.forward(size)
        t.left(90)
    t.forward(size*2)

def print_y(size):
    t.goto(0, size)
    t.left(130)
    t.forward(size)
    t.penup()
    t.backward(size)
    t.pendown()
    t.right(90)
    t.forward(size)
    t.penup()
    t.backward(size)
    t.pendown()
    t.right(130)
    t.forward(size)


def print_t(size):
    t.goto(0,size*2)
    t.left(90)
    t.forward(size*2)
    t.left(90)
    t.forward(size)
    t.right(180)
    t.forward(size*2)
    t.penup()


def print_h(size:int):
    t.goto(0, size*3)
    t.left(90)
    t.forward(size*2)
    t.backward(size)
    t.penup()
    t.right(90)
    t.pendown()
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.backward(size*2)
    t.penup()


def print_o(size:int):
    t.goto(0, size*4)
    for x in range(2):
       t.forward(size)
       t.left(90)
       t.forward(size*2)
       t.left(90)


def print_n(size:int):
    t.left(90)
    t.forward(size*2)
    t.right(140)
    t.forward(size*2.6)
    t.left(140)
    t.forward(size * 2)
