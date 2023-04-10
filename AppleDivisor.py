''' 

Problem Statement:-
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to 
distribute the apples. These “n” number of apples is provided to harry by his friends, and he can 
request for few more or a few less apples.
You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

Input:
Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisors of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5
2 is a divisor of20
3 is not a divisor of 20
…
5 is a divisor of 20
'''

#Taking Input
n = input("Enter the number of apples that Harry have got :: ")
mn = input("Enter the minimum number of students :: ")
mx = input("Enter the maximum number of students :: ")

#Checking if input is string
try:
    n = int(n)
    mn = int(mn)
    mx = int(mx)
except Exception as e :
    print("\nInvalid Input : Please give the input in number \n")
    exit()

#Checking if input is zero or negative 
if n==0 or mn == 0 or mx == 0:
    print("\n Invalid Input : Input can't be zero \n")
    exit()
if n<0 or mn < 0 or mx < 0:
    print("\n Invalid Input : Input can't be negative\n")
    exit()

#Processing
divisior = [ ]
if mn==mx:
    print("This must not be the range :: Maximum = Minimum")
    if(n/mn==int(n/mn)):
        print("Yes , it is the divisor")
        exit()
    else:
        print("NO, it is the divisor")
        exit()
else:
    for i in range(mn,mx+1):
        if(n/i==int(n/i)):
            print(f"{ i } is a divisor of { n }")
            divisior.append(i)
        else:
            print(f"{ i } is not a divisor of { n }")

#Output
print(" \n The divisor were :: \n")
for items in divisior:
    print(items)