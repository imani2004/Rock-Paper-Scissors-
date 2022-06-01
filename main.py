# Creating a game of rock,paper scissors
# R represents Rock, S represents Scissors and P represents Paper

game_list=["R","P","S"]
while True:
# let the user select a choice
 user_guess = input("Enter your choice:")
 if user_guess in ["R","P","S"]:
    print(input(user_guess))
    break
 else:
     print(input("Error, enter your choice:"))
     restart=user_guess
import random

#let the computer make their choice
computer_choice = random.choice(game_list)
#print out the result
print(f"Player({user_guess}):CPU({computer_choice})")
if user_guess==computer_choice:
    print(input("Enter your choice:"))

elif user_guess=="R":
            if computer_choice=="P":
                print("Computer wins")
            if computer_choice=="S":
                print("You won")
elif user_guess=="P":
            if computer_choice=="R":
                print("You won")
            if computer_choice=="S":
                print("Computer wins")
elif user_guess=="S":
            if computer_choice=="R":
                print("Computer wins")
            if computer_choice=="P":
                print("You win")
