"""
Problem Statement:-
Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of 
a given number and put one of the values (randomly generated) as wrong . Rohan Das did this to fool 
his classmates and make them commit a mistake in a test. You cannot 
tolerate this!So you decided to use your python skills to counter Rohan's actions by writing a python 
program that validates Rohan’s multiplication table.Your function should be able to find out the 
wrong values in Rohan’s table and expose Rohan Das as a fraud.

Note: Rohan's function returns a list of numbers like this

Rohan Das's Function Input:
rohanMultiplication(6)

Rohan's function returns this output:
[6, 12, 18,26,…., 60]

You have to write a function isCorrect(table, number) and return the index where rohan’s function is 
wrong and print it to the screen! If the table is correct, your function returns None
"""

import random

#Rohan Das Fraud Function
def rohan_das(n):
    b = random.randint(1,10)
    table = [ ]
    for i in range(1,11):
        if(i==b):
            table.append(random.randint(n,n*10))
        else:
            a = n*i
            table.append(a)
    return table

# Our's Rohan Das Fraud Function Checker
def IsCorrect(table,n):
    for i in range(1,11):
        a = i*n
        if(table[i-1]!=a):
            return f"Rohas Das's Multiplication Table is wrong at {i-1}th index"
    return None

#Input validator
def input_validator(n):
    try:
        n = int(n)
    except Exception as e :
        print("\nInvalid Input : Please give the input in number \n")
        exit()

#Input 
n = input("Enter the number , whose multiplication table you want ? :: ")
input_validator(n)
n = int(n)

#Invoking Rohan Das's Fraud Function
table = rohan_das(n)
print(f"\nRohan Das Fraud Multiplication Table :: {table} \n")

#Checking Rohan's Fraud
result = IsCorrect(table,n)
print(f"{result}\n")