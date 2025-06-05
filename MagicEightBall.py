#Angela Cai
#1/27/2025
#Magic 8 Ball

#Initialize
import random
import time
magic8list = ["Of course", "Most likely", "Most definitely!", "Never", "Perhaps", "No way", "Not so sure", "How did you know?!", "Definitely not", "Hah, in your dreams", "Yes", "No", "Never in a million years", "My sources say yes", "My sources say no"] #15 responses

#Functions
def MagicEightBallList():
    while True:
        print("Welcome to the Magic 8 Ball!")
        playersQuestion = (input("Enter a question that has been luring in your mind: "))
        if playersQuestion.endswith("?"):
            print("shake...")
            time.sleep(2)
            print("shake...")
            time.sleep(3)
            print("shake...")
            time.sleep(3)
            print(random.choice(magic8list))
        else:
            print("You must ask your question ending in a question mark")
        playersDecision = (input("Would you like to play again, yes or no?"))
        if playersDecision == "yes":
            print("Let's play again!")
        else:
            print("Byebye.")
            break
#Main
MagicEightBallList()
