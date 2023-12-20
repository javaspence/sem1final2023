import turtle as trtl
#import winsound
import time
import random
import keyboard
from death import Death

#sets up turtles
painter = trtl.Turtle()
clicker = trtl.Turtle()
help = trtl.Turtle()
fastfood = trtl.Turtle()
text = trtl.Turtle()
moneytext = trtl.Turtle()
heavenlytext = trtl.Turtle()
heavenlytext2 = trtl.Turtle()
yearstext = trtl.Turtle()
healthtext = trtl.Turtle()
happinesstext = trtl.Turtle()
medicine = trtl.Turtle()
sell = trtl.Turtle()
movies = trtl.Turtle()
screen = trtl.Screen()

screen.setup(1040, 850)
screen.screensize(1003, 800)
screen.addshape('pictures/Intro1.gif')

#add shapes
screen.addshape('pictures/Present.gif')
screen.addshape('pictures/GenerousPresent.gif')
screen.addshape('pictures/Sell.gif')
screen.addshape('pictures/Medicine.gif')
screen.addshape('pictures/fastfood.gif')
screen.addshape('pictures/Movies.gif')
screen.addshape('pictures/NoMovies.gif')

#set up text, help, etc.
text.penup()
text.hideturtle()
text.goto(-55, 330)
moneytext.penup()
moneytext.hideturtle()
moneytext.goto(-55, 300)
heavenlytext.penup()
heavenlytext.hideturtle()
heavenlytext.goto(50, 270)
heavenlytext2.penup()
heavenlytext2.hideturtle()
heavenlytext2.goto(-55, 270)
yearstext.penup()
yearstext.hideturtle()
yearstext.goto(-55, 240)
healthtext.penup()
healthtext.hideturtle()
healthtext.goto(-55, 210)
happinesstext.penup()
happinesstext.hideturtle()
happinesstext.goto(-55, 180)
help.penup()
help.hideturtle()
help.goto(300, 300)
help.shape('pictures/GenerousPresent.gif')
sell.penup()
sell.hideturtle()
sell.goto(300, 150)
sell.shape('pictures/Sell.gif')
medicine.penup()
medicine.hideturtle()
medicine.goto(-300, 300)
medicine.shape('pictures/Medicine.gif')
clicker.hideturtle()
clicker.shape('pictures/Present.gif')
clicker.shapesize(0.75)
fastfood.penup()
fastfood.hideturtle()
fastfood.goto(-300, 150)
fastfood.shape('pictures/fastfood.gif')
movies.penup()
movies.hideturtle()
movies.goto(-300, 0)
movies.shape('pictures/Movies.gif')


def introstart(x, y):
  painter.hideturtle()
  text.write('Presents: 0', font=("Verdana", 15, "normal"))
  moneytext.write('Money: 0', font=("Verdana", 15, "normal"))
  heavenlytext.write('0', font=("Verdana", 15, "normal"))
  heavenlytext2.write('Heavenly:', font=("Verdana", 15, "normal"))
  yearstext.write('Years: 0', font=("Verdana", 15, "normal"))
  healthtext.write('Health: 100', font=("Verdana", 15, "normal"))
  happinesstext.write('Happiness: 100', font=("Verdana", 15, "normal"))
  help.showturtle()
  sell.showturtle()
  medicine.showturtle()
  clicker.showturtle()
  fastfood.showturtle()
  movies.showturtle()

painter.goto(0,0)
painter.shape('pictures/Intro1.gif')
painter.onclick(introstart)
   
#set up variables
presents = 0
presentscounter = 0
moviescounter = 0
banmovies = False
years = 0
money = 0
heavenly = 0
health = 100
healthsubtractor = 1
happiness = 100

def clicked(x, y):
  global presents, presentscounter, years, health, healthsubtractor, happiness, moviescounter, banmovies
  presents = presents + 1
  presentscounter = presentscounter + 1
  if moviescounter == 3:
    banmovies == True
    movies.shape('pictures/NoMovies.gif')
  text.clear()
  text.goto(-55, 330)
  text.write(f'Presents: {presents}', font=("Verdana", 15, "normal"))
  if presentscounter == 5:
    years = years + 1
    presentscounter = 0
    movies.shape('pictures/Movies.gif')
    moviescounter = 0
    banmovies == False
    yearstext.clear()
    yearstext.write(f'Years: {years}', font=("Verdana", 15, "normal"))
    if years >= 18:
        health = health - healthsubtractor
        healthsubtractor = healthsubtractor + 0.25
        healthtext.clear()
        healthtext.write(f'Health: {health}', font=("Verdana", 15, "normal"))
    if years >= 12:
        happiness = happiness - 10
        happinesstext.clear()
        happinesstext.write(f'Happiness: {happiness}', font=("Verdana", 15, "normal"))
  if (int(health) < 0) == True:
    #if heavenly < 0:
      #Death.hell()
    if heavenly > 0:
      painter.hideturtle()
      clicker.hideturtle()
      help.hideturtle()
      fastfood.hideturtle()
      text.hideturtle()
      moneytext.hideturtle()
      heavenlytext.hideturtle()
      heavenlytext2.hideturtle()
      yearstext.hideturtle()
      healthtext.hideturtle()
      happinesstext.hideturtle()
      medicine.hideturtle()
      sell.hideturtle()
      movies.hideturtle()
      text.clear()
      moneytext.clear()
      heavenlytext.clear()
      heavenlytext2.clear()
      yearstext.clear()
      healthtext.clear()
      happinesstext.clear()
      Death.heaven()
    else:
      painter.hideturtle()
      clicker.hideturtle()
      help.hideturtle()
      fastfood.hideturtle()
      text.hideturtle()
      moneytext.hideturtle()
      heavenlytext.hideturtle()
      heavenlytext2.hideturtle()
      yearstext.hideturtle()
      healthtext.hideturtle()
      happinesstext.hideturtle()
      medicine.hideturtle()
      sell.hideturtle()
      movies.hideturtle()
      text.clear()
      moneytext.clear()
      heavenlytext.clear()
      heavenlytext2.clear()
      yearstext.clear()
      healthtext.clear()
      happinesstext.clear()
      Death.Hell()
  if (int(happiness) < 0) == True:
      print('test')
      if heavenly > 0:
        painter.hideturtle()
        clicker.hideturtle()
        help.hideturtle()
        fastfood.hideturtle()
        text.hideturtle()
        moneytext.hideturtle()
        heavenlytext.hideturtle()
        heavenlytext2.hideturtle()
        yearstext.hideturtle()
        healthtext.hideturtle()
        happinesstext.hideturtle()
        medicine.hideturtle()
        sell.hideturtle()
        movies.hideturtle()
        text.clear()
        moneytext.clear()
        heavenlytext.clear()
        heavenlytext2.clear()
        yearstext.clear()
        healthtext.clear()
        happinesstext.clear()
        Death.heaven()
      else:
        painter.hideturtle()
        clicker.hideturtle()
        help.hideturtle()
        fastfood.hideturtle()
        text.hideturtle()
        moneytext.hideturtle()
        heavenlytext.hideturtle()
        heavenlytext2.hideturtle()
        yearstext.hideturtle()
        healthtext.hideturtle()
        happinesstext.hideturtle()
        medicine.hideturtle()
        sell.hideturtle()
        movies.hideturtle()
        text.clear()
        moneytext.clear()
        heavenlytext.clear()
        heavenlytext2.clear()
        yearstext.clear()
        healthtext.clear()
        happinesstext.clear()
        Death.Hell()


def helpclicked(x, y):
  global presents, heavenly
  if presents > 0:
    presents = presents - 1
    text.clear()
    text.goto(-55, 330)
    text.write(f'Presents: {presents}', font=("Verdana", 15, "normal"))
    heavenly = heavenly + 1
    if heavenly < 0:
        heavenlytext.color('red')
    if heavenly == 0:
        heavenlytext.color('black')
    if heavenly > 0:
        heavenlytext.color('green')
    heavenlytext.clear()
    heavenlytext.write(f'{heavenly}', font=("Verdana", 15, "normal"))


def sellclicked(x, y):
  global money, presents, heavenly
  weightlist = ([20] * 60) + ([50] * 25) + ([100] * 15)
  moneycost = 0
  thechoice = random.choice(weightlist)
  if thechoice == 20:
    moneycost = random.randint(1, 20)
  if thechoice == 50:
    moneycost = random.randint(20, 50)
  if thechoice == 100:
    moneycost = random.randint(50, 100)
  if presents > 0:
    presents = presents - 1
    money = money + moneycost
    text.clear()
    text.goto(-55, 330)
    moneytext.clear()
    moneytext.goto(-55, 300)
    text.write(f'Presents: {presents}', font=("Verdana", 15, "normal"))
    moneytext.write(f'Money: {money}', font=("Verdana", 15, "normal"))
    heavenly = heavenly - 1
    if heavenly < 0:
        heavenlytext.color('red')
    if heavenly == 0:
        heavenlytext.color('black')
    if heavenly > 0:
        heavenlytext.color('green')
    heavenlytext.clear()
    heavenlytext.write(f'{heavenly}', font=("Verdana", 15, "normal"))

def medicineclicked(x, y):
  global money, heavenly, health
  if money >= 1000:
    money = money - 1000
    moneytext.goto(-55, 300)
    moneytext.clear()
    moneytext.write(f'Money: {money}', font=("Verdana", 15, "normal"))
    health = health + (health * .5)
    if health > 100:
        health = 100
    healthtext.clear()
    healthtext.write(f'Health: {health}', font=("Verdana", 15, "normal"))

def fastfoodclicked(x, y):
  global money, heavenly, health, happiness
  if money >= 20:
    money = money - 20
    moneytext.goto(-55, 300)
    moneytext.clear()
    moneytext.write(f'Money: {money}', font=("Verdana", 15, "normal"))
    happiness = happiness + 5
    if happiness > 100:
        happiness = 100
    happinesstext.clear()
    happinesstext.write(f'Happiness: {happiness}', font=("Verdana", 15, "normal"))
    health = health - 5
    healthtext.clear()
    healthtext.write(f'Health: {health}', font=("Verdana", 15, "normal"))

def moviesclicked(x, y):
  global money, heavenly, happiness, banmovies, moviescounter
  if moviescounter == 3:
    banmovies == True
    movies.shape('pictures/NoMovies.gif')
  if banmovies == False:
    if money >= 30:
      moviescounter = moviescounter + 1
      money = money - 30
      moneytext.goto(-55, 300)
      moneytext.clear()
      moneytext.write(f'Money: {money}', font=("Verdana", 15, "normal"))
      happiness = happiness + 10
      if happiness > 100:
        happiness = 100
      happinesstext.clear()
      happinesstext.write(f'Happiness: {happiness}', font=("Verdana", 15, "normal"))
  


#create present
clicker.onclick(clicked)
help.onclick(helpclicked)
sell.onclick(sellclicked)
medicine.onclick(medicineclicked)
fastfood.onclick(fastfoodclicked)
movies.onclick(moviesclicked)
keyboard.on_press_key("space", lambda _:clicked(0, 0))
#for song in range(2):
    #if song == 1:
        #winsound.PlaySound('Yuno Miles - First Day Of Christmas (Official Video) (Prod.YunoMarr) (1).wav', winsound.SND_ASYNC)
    #else:
        #winsound.PlaySound('Yuno Miles - Indiana Jones (Official Video).wav', winsound.SND_ASYNC)


screen.mainloop()
