#Angela Cai
#1/29/2025
#Slot Machine
#Init
symbols = ["⚡","💞", "7", "3"]
credits = 100
spins = 100
import random
import time

#Functions
def SlotMachine():
    global symbols
    global credits
    global spins
    while True:
        print("Welcome to the 3-Slot Machine!")
        print("You begin with 100 credits!")
        playersDecision = input("Would you like to spin or quit?")
        if playersDecision == "spin":
            time.sleep(1)
            print("rumble...")
            time.sleep(1)
            symbols1 = (random.choices(symbols, weights = [10, 10, 3, 1], k = 1))
            time.sleep(1)
            print("rumble...")
            time.sleep(1)
            symbols2 = (random.choices(symbols, weights = [10, 10, 3, 1], k = 1))
            time.sleep(1)
            print("rumble...")
            time.sleep(1)
            symbols3 = (random.choices(symbols, weights = [10, 10, 3, 1], k = 1))
            print(str(symbols1) + " " + str(symbols2) + " " + str(symbols3))
        else:
            print("GoodBye.")
            break

        if playersDecision == "spin":
            print("You have lost 10 credits from spinning.")
            spins = spins - 10
            print("You now have " + str(spins) + " credits.")

        if symbols == "7":
            print("You have won the Slot Machine Game!")
            print("You have earned 10 credits from getting all 7's!")
            credits = credits + 10
            print("You now have " + str(credits) + " credits.")
        elif symbols == "3":
            print("JACKPOT!")
            print("WOW! You have won 200 credits from getting JACKPOT. Congratulations!!!")
            credits = credits + 100
            print("You now have " + str(credits) + " credits.")
        elif symbols == "💞" and symbols == "💞" and symbols == "💞" or symbols == "⚡" and symbols == "⚡" and symbols == "⚡":
            print("Oh no, you lost the game.")
            print("You lost 20 credits.")
            credits = credits - 20
            print("You still have " + str(credits) + " credits.")
        else:
            print("Oh no, you lost the game.")
            print("You lost 20 credits because you did not win and did not have any numbers too.")
            credits = credits - 20
            print("You still have " + str(credits) + " credits.")
            print("Sorry, you can no longer play this Slot Machine since you do not have enough credits.")
            print("Please pay more in order to continue playing.")
            print("Hope to see you soon!")

        if credits == "0":
            print("Sorry, you can no longer play this Slot Machine since you do not have enough credits.")
            print("Please pay more in order to continue playing.")
            print("Hope to see you soon!")
        else:
            print("You can keep on playing!")
#Main
SlotMachine()

#1. Introduction
#2. Ask the player, spin or quit
#3. Randomly pull three items from your list
#ADVICE: Make sure you store these in a variable
#4 Determine the outcome (IF ELIF ELSE)

#Start the player with 100 credits
#Every spin costs 10 choice credits
#Jackpot = +100 reward(own choice for #)
# 3 of a kind is +10 credits
# 2 of a kind = +2 credits
#Display their credits consistetnly
#Do not let them play with 0 credits
