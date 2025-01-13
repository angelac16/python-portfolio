#Name: Angela Cai
#Date: 12/11/2024

#Initialize
import turtle
angela = turtle.Turtle()

#Functions
def draw_ticket(name, price, dayofweek, y_location):
    angela.goto(-50, y_location)
    angela.write("Ticket", font=("Arial", 15), align="right")
    angela.pendown()
    for i in range(2):#the rectangular shape of the ticket drawn
        angela.forward(500)
        angela.left(90)
        angela.forward(250)
        angela.left(90)
    angela.penup()#the rectangular shape of the ticket drawing ends here
    angela.goto(50, y_location +215)
    angela.write("Admit One", font=("Arial", 15), align="right")
    angela.goto(440, y_location +215)
    angela.write(dayofweek, font=("Arial", 15), align="right")
    angela.goto(225, y_location +135)
    angela.write(name, font=("Arial", 15), align="right")
    angela.goto(225, y_location +15)
    angela.write(price, font=("Arial", 15), align="right")
    print("Welcome to the Movie Theater!")#the location is at a movie theater
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
day = input("Please enter the day of the week in all lowercase letters: ")
freefriday = input("Please enter yes if you have the freefriday coupon and no if you do not in all lowercase letters: ")
sunday10 = input("Please enter yes if you have the sunday10 coupon and no if you do not in all lowercase letters: ")
if age <=3:#if one's age is less than three
    price = 0#the price of the ticket is $0
    print("Your ticket is 0 dollars, hope you enjoy the movie today!")
elif age > 3 and age < 18 and day == "friday" and freefriday == "yes":#if one's age is greater than 3 but less than 4, the day is friday, and if they have the free friday coupon
    price = 0#the price of the ticket is $0
    print("Your ticket is 0 dollars, hope you enjoy the movie today!")
elif age > 3 and age < 18 and day == "sunday" and sunday10 == "yes":
    price = 90#the price of the ticket is $90
    print("Your ticket is 90 dollars, please pay the full amount to recieve your ticket.")
elif age > 3 and age < 18 and day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    price = 50#the price of the ticket is $50
    print("Your ticket price is 50 dollars, please pay the full amount to recieve your ticket.")
elif age > 3 and age < 18 and day == "saturday" or day == "sunday":
    price = 100#the price of the ticket is $100
    print("Your ticket price is 100 dollars, please pay the full amount to recieve your ticket.")
elif age > 17 and day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    price = 100#the price of the ticket is $100
    print("Your ticket price is 100 dollars, please pay the full amount to recieve your ticket.")
elif age > 17 and day == "saturday" or day == "sunday":
    price = 100#the price of the ticket is $100
    print("Your ticket price is 100 dollars, please pay the full amount to recieve your ticket.")

#Main
draw_ticket(name,price,day,0)
