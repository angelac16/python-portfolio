#Angela Cai
#11/18/2024
#Simple Calculator

#Init
#Functions
#Adds two numbers together and prints the result
def add(num1, num2):
    result = num1 + num2 #This function is to add two numbers together
    print(result)#This is what causes the dividing to be seen for the player. 
def subtract(num1, num2):
    result = num1 - num2 #This function is to subtract two numbers from each other.
    print(result)#This is what causes the dividing to be seen for the player.
def multiply(num1, num2):
    result = num1*num2 #This function is to multiply two numbers together
    print(result)#This is what causes the dividing to be seen for the player.
def divide(num1, num2):
    result = num1/num2 #This function is to divide two numbers
    print(result) #This is what causes the dividing to be seen for the player.

print("Welcome to simple calculator")
def simpleCalculator():
    while True:
        print("Please select an operation: ") #This is for the player to pick which operation they want to use on the calculator
        print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit""")
        operation = int(input("(1-5) Option: "))
        if operation == 1:
            int1 = int(input("Enter the first number: "))#The player enters their first number
            int2 = int(input("Enter the second number: "))#The player enters their second number
            add(int1, int2) #This function is to add two numbers together
        elif operation == 2: #If they typed in "2", they picked the subtraction function on the calculator
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            subtract(int1, int2)
        elif operation == 3: #If they typed in "3", they picked the multiplication function on the calculator
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            multiply(int1, int2)
        elif operation == 4: #If they typed in "2", they picked the division function on the calculator
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            divide(int1, int2)
        elif operation == 5: #If they typed in "2", they picked the quit button on the calculator
            print("Goodbye.")
            break #This ends the continuous loop of using the calculator.

#Main
simpleCalculator()
