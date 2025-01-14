#Angela Cai
#1/9/2025
#Multiplication Quiz

#Init
import random
score = 0

#Functions
def multiplication_quiz():
    print("Welcome to the Multiplication Quiz!") #Welcoming the player
    amountOfQuestions = int(input("How many multiplication questions would you like?: "))#The player decides on how many questions they want to be asked.
    for i in range(amountOfQuestions):
        num1 = random.randint(1,20) #Integer
        num2 = random.randint(1,20) #Integer
        print("What is " + str(num1) + " x " + str(num2)) #Converting the number to a string to add the strings with the numbers together
        playersAnswer = int(input("Please enter your answer: "))
        solution = num1*num2#This multiplies two numbers together, but does not show the audience what the solution is.
        if playersAnswer == solution:
            global score#Global allows to change a variable value wherever it is and needed.
            print("Yay, you are correct!")#The player got the multiplication question right.
            score = score + 1#This is a score baord to keep track of the score when the player gets a question right each time.
        else:
            print("Oh no, you got it incorrect.")#The player got the answer wrong for the question.
        print("Your score is " + str(score) + " out of " + str(amountOfQuestions))#This is the player's total score at the end of the game

#Main
multiplication_quiz()


