import os

# Starting the game
inventory = []
skills = []
print("Hello welcome to Adventure Land")
print("Before you start please litsen to these rules,\nrule 1: All quenstions are going to be answered with a 1 or 2 or sometimes 3 if you dont type one of those in the game may have a bug or a glitch")
print("Get ready for a long and fun adventure")


# The first choice and the biggest one in the game
begin = int(input("You wake up in a dark room with no windows and only one light above your head there are 2 doors to your side to your right and left what do you choose \n1) left \n2) right: "))

# What friend you meet
def begin1():
  if begin == 1:
    name = input("You turn to your left and open the door and you see another person they ask for your name you say: ")
    print("They say nice to meet you ",str(name)," my name is Valery")
    print("I found a bow I guess ill keep in just in case")
  if begin == 2:
    name = input("You turn to your right and open the door and you see another person they ask for your name you say: ")
    print("They say nice to meet you ",str(name)," my name is Zachery")
    print("I found a sword I guess ill keep in just in case")
  ready = int(input("enter 1 when your ready to move on: "))
  if ready == 1:
    clear = lambda:os.system('clear')
    clear()
    
begin1()

# Get your weapon
weapon = int(input("Your new ally says that they have found a \n1)Sword \n2)Bow \n3)Wand and they say you can have one as well what do you choose"))
if weapon == 1 :
  print("You got a Sword")
  inventory.append("sword")
if weapon == 2 :
  print("you got a Bow")
  inventory.append("bow")
if weapon == 3 :
  print("you got a Wand")
  inventory.append("wand")
    
#Escape choice
print("You and your new ally deside to find a way out")
UpOrDown = int(input("You and your ally find a hole in the roof with a rope that you can climb and a hole that you can jump down what do you choose \n1) roof \n2) ground \n3) stay: "))
x = 0
def zr(x):
  x += 1


def rgs():
  if UpOrDown == 3:
    print("You stay in the room and lose your life to starvation")
    print("GAME OVER")
    quit()
  elif UpOrDown == 2:
    print("You go down and see a snake")
    krt = int(input("Do you \n1) attak it \n2) run \n3) mystery choice: "))
    if krt == 3:
      print("You tame it and move on with your friend")
      zr(x)
      inventory.append("pet")
    if krt == 2:
      print("You kill it and move on with your friend, but you and your friend grow stronger")
    if krt == 1:
      print("You run from it and move on with your friend, but did not achevie anything from this")
  elif UpOrDown == 1:
    print("You go down and see a dragon")
    krt = int(input("Do you \n1) attak it \n2) run \n3) mystery choice: "))
    if krt == 3:
      print("You tame it and move on with your friend")
      zr(x)
      inventory.append("pet")
    if krt == 2:
      print("You kill it and move on with your friend, but you and your friend grow stronger")
    if krt == 1:
      print("You run from it and move on with your friend, but did not achevie anything from this")

rgs()

ready = int(input("Enter 1 when your ready to move on: "))
if ready == 1:
    clear = lambda:os.system('clear')
    clear()
# Village
print("You and you friend walk around and find a way out")
path = int(input("You find a path \n1) follow it \n2) try to find somthing else"))
if path == 1:
  print("You find a village =)")
else:
  print("You get lost in the woods and get attaked by wild animals")
  print("GAME OVER")
  quit()

print("In the village you find villagers living a normal life")
print("you and your friend walk up to one and ask if you two can stay there")
village = int(input("The villager responds and says only if they help protect the village from the animals that may come in do you \n1) accept \n2) decline"))
if village == 1:
  print("The villagers welcome you with open arms")
else:
  print("you find out the village is a secret village and they dont want other people to know that they are alive so they attak you and your friend ")
  print("GAME OVER")
  quit()
if ready == 1:
    clear = lambda:os.system('clear')
    clear()

#Village attak

print("Your sleeping in your bed and you here a lot of noises. A villager comes up to you and says the village is under attak")
monster = int(input("You ask him what has attaked the village and he says \n1) Bear \n2) Giant Crow \n3) Evil Wizard"))
def FIGHT():
  if monster == 1:
    print("Your friend asks you if they should attak it of should you attak it")
    life = int(input("\n1) You \n2) Friend"))
    if life == 1:
      print("You are about to get attaked but your friend saves you and both of you make it out alive")
    if life == 2:
      print("Your friend gets scared and runs and you get attaked")
      print("GAME OVER")
      quit()
  if monster == 2:
    print("Your friend asks you if they should attak it of should you attak it")
    life = int(input("\n1) You \n2) Friend"))
    if life == 1:
      print("You are about to get attaked but your friend saves you and both of you make it out alive")
    if life == 2:
      print("Your friend gets scared and runs and you get attaked")
      print("You live and lose your friend")
  if monster == 3:
    print("Your friend asks you if they should attak it of should you attak it")
    life = int(input("\n1) You \n2) Friend"))
    if life == 1:
      print("You are about to get attaked but your friend saves you and both of you make it out alive")
    if life == 2:
      print("Your friend is about to attak him but than he says that if they spare him he will give them a special power")
      power = int(input("\n1) aceppt \n2) decline"))
      if power == 1:
        print("You got a new ability called heal")
        skills.append("heal")
        if inventory[0] == "pet":
          print("Your pet became a healing pet")
      if power == 2:
        print("He runs away before you can get him")

FIGHT()
print("Your adventure ends and you live happliy ever after or do you...")