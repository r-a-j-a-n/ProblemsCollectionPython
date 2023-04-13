"""
Problem Statement ::

Generate a random integer from a to b. You and your friend have to guess a number between two 
numbers, a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He 
will have to keep choosing the number, and your program must tell whether the number is greater than 
the actual number or less than the actual number. Log the number of trials it took your friend to 
arrive at the number. You play the same game, and then the person with the minimum number of trials 
wins! Randomly generate a number after taking a and b as input and don’t show that to the user.

Input:
Enter the value of a
4
Enter the value of b
13

Output:
Player1 :
Please guess the number between 4 and 13
5
Wrong guess a greater number again
8
Wrong guess a smaller number again
6
Correct, you took 3 trials to guess the number
Player 2:
Correct, you took 7 trials to guess the number
Player 1 wins!
"""
#Importing the required modules
import random

#Validating the Input
def input_validator(b):
    """Function to check whether the input is valid or not.(i.e STRING is invalid here)"""
    try:
     c = int(b)
    except Exception as e :
        print("\nInvalid Input : Please give the input in number \n")
        exit()



#Input
a = input("Enter the 1st number :: ")
input_validator(a)
a = int(a)
b = input("Enter the 2nd number :: ")
input_validator(b)
b = int(b)

#Processing :
player1_trial = 1
player2_trial = 1

actual_num = random.randint(a,b)

print("\nPlayer 1 :")
print(f"Guess the number between {a} and {b}")
while(True):
   num = input("Enter your guessed number ::")
   input_validator(num)
   num = int(num)
   if(num == actual_num):
      print("Correct Guess")
      break
   elif(num<actual_num):
      print("Guess the larger number again")
   elif(num>actual_num):
      print("Guess the smaller num again")
   player1_trial = player1_trial + 1

actual_num = random.randint(a,b)
print("\nPlayer 2 :")
print(f"Guess the number between {a} and {b}")
while(True):
   num = input("Enter your guessed number ::")
   input_validator(num)
   num = int(num)
   if(num == actual_num):
      print("Correct Guess")
      break
   elif(num<actual_num):
      print("Guess the larger number again")
   elif(num>actual_num):
      print("Guess the smaller num again")
   player2_trial = player2_trial + 1

#Output :
if player1_trial>player2_trial:
   print("\nPLayer 2 wins")
elif player1_trial<player2_trial:
   print("\nPLayer 1 wins")
else:
   print("\nDraw")