"""
Problem Statement:-
It's result day at school and not everyone is happy. You decided to make your friends laugh by 
jumbling their names to come up with some funny names.Your program should take the number of names 
and the names separated by space as input. Output should be funny names in the same order.

Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal

"""
import random
#Input validator
def input_validator(n):
    try:
        n = int(n)
    except Exception as e :
        print("\nInvalid Input : Please give the input in number \n")
        exit()

names = []
first_name = []
second_name = []
#Taking Input
n = input("Enter number of friends :: ")
input_validator(n)
n = int(n)
for i in range(1,n+1):
    a = input("\nEnter the name :: ")
    names.append(a)

for items in names:
    splitted_names = items.split()
    first_name.append(splitted_names[0])
    second_name.append(splitted_names[1])

for items in first_name:
    a = random.randint(0,n-1)
    print(f"{items} {second_name[a]}")