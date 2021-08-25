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
name = input("What is your name?\n")

first_test = input("You are at a fork in the road. Would you like to go right or left?\n").lower()

if first_test == 'right':
    print("You fell into a hole. Game Over. You suck.")
elif first_test == 'left':
    print("You went the right way. You may continue on your journey.")
    second_test = input("You have reached a beach and see an island in the distance. Would you like to swim to the island or wait for a boat? Type 'swim' or 'wait'\n").lower()
    if second_test == 'swim':
        print("You were eaten by piranhas. Game Over. You suck.")
    elif second_test == 'wait':
        print("The boat came and you reached the island safely. You may continue on your journey.")
        third_test = input("You have reached a room with 3 different doors. If you choose poorly, you will die. If you choose correctly, you will find the treasure.\nChoose a door: yellow, red or blue.\n").lower()
        if third_test == 'red':
            print("You were burned alive by a demon. Game Over. You suck.")
        elif third_test == 'yellow':
            print(f"Congratulations, {name}! You found the treasure. You win!")
        elif third_test == 'blue':
            print("You were eaten alive by rabid dogs. Game Over. You suck.")
        else:
            print("You got stuck and starved to death. Game Over. You suck")





#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload