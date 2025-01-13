#Angela Cai
#1/9/2025
#Multiplication Quiz

#Init
import random
score = 0

#Functions
def multiplication_quiz():
    print("Welcome to the Multiplication Quiz!") #Welcoming the player
    amountOfQuestions = int(input("How many multiplication questions would you like?: "))
    for i in range(amountOfQuestions):
        num1 = random.randint(1,20) #Integer
        num2 = random.randint(1,20) #Integer
        print("What is " + str(num1) + " x " + str(num2)) #Converting the number to a string to add the strings with the numbers together
        playersAnswer = int(input("Please enter your answer: "))
        solution = num1*num2
        if playersAnswer == solution:
            global score
            print("Yay, you are correct!")
            score = score + 1
        else:
            print("Oh no, you got it incorrect.")
        print("Your score is " + str(score) + "out of " + str(amountOfQuestions))

#Main
multiplication_quiz()

