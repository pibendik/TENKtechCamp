import turtle 
#oppgave 1: tegn skilpadden 

skilpadde = turtle.Turtle() 
skilpadde.shape("turtle") 
skilpadde.color("lightgreen", "green") 

#oppgave 2 og 3: terning 
terning = [1,2,3,4,5,6] 
 
import random 
def kast_terning(): 
  terningkast = random.choice(terning) 
  print("du kastet " + str(terningkast)) 
  return terningkast 

#oppgave 4: målstrek 
målstrek = turtle.Turtle()  
målstrek.color("red")  
målstrek.penup()  
målstrek.goto(150,-300)  
målstrek.pendown()  
målstrek.goto(150,300)  
målstrek.penup()  

#oppgave 5: flytt skilpadden 
skilpadde.penup() 
posX = -150 
posY = 0 
skilpadde.goto(posX, posY) 
 
#oppgave 6: lag spillvariabler 
poeng = 100 
runde = 1 
 
#oppgave 7, 8 og 9: spillet 
while runde < 100: 
  print("Runde " + str(runde))  
  runde += 1 
  poeng -= 1  
  if skilpadde.pos() > (150,0):  
    print("Du har vunnet") 
    print("Du fikk " + str(poeng) + " poeng")  
    break  
  else:  
    kast = input("trykk enter for å kaste terning")  
    terningkast = kast_terning()  
    posX = posX + terningkast  
    skilpadde.goto(posX, 0) 
 
print("Game over") 