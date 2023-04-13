"""A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
676, 616, mom, 100001.
You have to take a number as an input from the user. You have to find the next palindrome 
corresponding to that number. Your first input should be the number of test cases and then take all 
the cases as input from the user. 

Input:
n =3

451
10
2133

Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2311 is 2222"""

def input_validator(b):
    """Function to check whether the input is valid or not.(i.e STRING is invalid here)"""
    try:
     c = int(b)
    except Exception as e :
        print("\nInvalid Input : Please give the input in number \n")
        exit()

n = input("How many test cases? \n ")
input_validator(n)

for i in range(1,int(n)+1):
    a = input("Enter the number :: ")
    input_validator(a)
    j = int(a)
    while(j!=0):
        d  = str(j)
        d = d[::-1]
        if(j==int(d)):
           print(f"Next palindrome for {a} is {d} \n")
           break
        j = j+1