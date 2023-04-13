"""
Problem Statement:-
You are given a list that contains some numbers. You have to print a list of the next palindromes 
only if the number is greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
"""

#Validating the Input
def input_validator(b):
    """Function to check whether the input is valid or not.(i.e STRING is invalid here)"""
    try:
     c = int(b)
    except Exception as e :
        print("\nInvalid Input : Please give the input in number \n")
        exit()

#Declaring the lists
num_list = [ ]
num_out = [ ]

#Input :
n = input("How many numbers you wanna enter ?")
input_validator(n)
n = int(n)
for i in range(1,n+1):
   num = input("Enter the number :: ")
   input_validator(num)
   num = int(num)
   num_list.append(num)

#Processing
for items in num_list:
    j = items
    while(j!=0):
        d  = str(j)
        d = d[::-1]
        if(j==int(d)):
           num_out.append(j)
           break
        j = j+1

#Output
print(num_out)