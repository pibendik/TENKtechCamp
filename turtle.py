import turtle
import random
skilpadde = turtle.Turtle()
skilpadde.shape("turtle")
skilpadde.color("lightgreen", "green")
skilpadde.penup()
posX = -150
posY = 0
skilpadde.goto(posX, posY)
mål = turtle.Turtle()
mål.color("red")
mål.penup()  # skriv forklaring på denne
mål.goto(150, -300)
mål.pendown()
mål.goto(150, 300)
mål.penup()
# terning
terning = [1, 2, 3, 4, 5, 6]


def kast_terning():


terningkast = random.choice(terning)
print("du får flytte " + str(terningkast) + " steg")
return terningkast
# poeng
poeng = 10
# spill
runde = 1
while runde < 100:
print("Runde: " + (str(runde)))
if skilpadde.pos() > (150, 0):
print("Du har vunnet")
print("Du fikk " + str(poeng) + " poeng")
break
else:
kast = input("trykk enter for å kaste terning")
terningkast = kast_terning()
posX = posX + terningkast
skilpadde.goto(posX, posY)
runde += 1
poeng -= 1
