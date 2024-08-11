print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("Where do you wanna go 'left' or 'right'? Type 'left' or 'right' ")
dir = direction.lower()
if dir == "left":
  print("You reached the docks of the island do you want to 'wait' or 'swim'?")
  choose = input("Type 'wait' or 'swim'")
  if choose == "wait":
    print("when you waited u saw a boat with that u reached a place with three doors 'red' , 'blue' and 'yellow'")
    door = input("choose a door. Type 'red' 'blue' or 'yellow' ")
    door_choice = door.lower()
    if door_choice == "red":
       print("As soon as you opened the door the burning flames engulfed you and u died \n Game over...")
    elif door_choice == "blue":
       print("The minute u entered the blue room u turned into ice cus of the freezing temperature \n Game Over... ")
    elif door_choice == "yellow":
        print("YESSS LETS GOO!!! You got the treasure my friend!! You won!!!") 
    else:
      print(" You have chosen a door that's non existent :( . Game Over... ")
  else:
    print("Oops you got eaten by an hungry shark lurking in the water!! Game Over...")
else:
  print("Oh Oh you fell into a hole! Game Over...")