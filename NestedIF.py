#Angela Cai
#10/18/2024

print("Welcome to Your Winter or Summer Name!")
print("Answer the questions to find out if you have a Winter or Summer Name")
ans = input("Alaska (a) or Hawaii (h) ?")
if ans == "a":
    ans = input("Winter (w) or Mountain (m) ?")#If the player picks w, then they will be a winter.
    if ans == "w":
        ans = input("Bears (be) or Blue (bl) ?")#Since the player picked w, they can either pick Bears or Blue.
        if ans == "be":
            print("Your first name is Wasers")#If they picked w, then their name is Wasers.
        else:
            print("Your first name is Luert")#If the player did not pick be, then their name is Luert.
if ans == "a":#The player picks a for Alaska instead of h for Hawaii.
    ans = input("Winter (w) or Mountain (m) ?")#The player has an option to pick the Winter or mountain.
    if ans == "m":#The player chooses m
        ans = input("Snow (s) or Tree (t) ?")#The player has an option to pick s for Snow or t for Tree.
        if ans == "s":
            print("Your first name is Snotain")#The player picked snow so their name is Snotain.
        else:
            print("Your first name is Tretain")#The player picked t so their name is Tretain.
if ans == "h":
    ans = input("Palms (p) or Beach (b) ?")#The player has the option to pick between palms and beach because they picked Hawaii (a summer location)
    if ans == "p":
        ans = input("Coconut (c) or Berry (b) ?")#The player picked palms and now get to decide whether they want ot pick coconut or berry.
        if ans == "c":
            print("Your first name is Palconut")#The player chooses coconut so their name is now Palcoconut.
        else:
            print("Your first name is Palberry")#The player chose berry so their name is now Palberry.
if ans == "h":
    ans = input("Palms (p) or Beach (b) ?")
    if ans == "b":#The player picked b for beach.
        ans = input("Sand (s) or Palm (P) ?")#The player has an option to pick s for sand or p for palm.
        if ans == "s":#The player picked s for Sand.
            print("Your first name is Achand")#The players name is Achand.
        else:
            print("Your first name is Treeach")#The player did not choose s for sand so their name is Treeach.
