"""
Problem Statement:-

You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, 
based on their amount of calories. You have to reserve this list of food items containing calories.
You have to use the following three methods to reserve a list:
    1.Inbuild method of python
    2.List name [::-1] slicing trick
    3.Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]
"""

calorie_list = [ ]

#Input
n = int(input("Enter how many food items you do have :: "))
print("Enter the calories ")
for i in range(1,n+1):
    calorie_list.append(int(input()))

calorie_list.sort()

#Inbuilt method
calorie_list_1 = calorie_list.copy()
calorie_list_1.reverse()

#List slicing method
calorie_list_2 = calorie_list[::-1]

#Swapping first with last element and others elements as well
calorie_list_3 = calorie_list[::]
c = n-1
for i in range(n):
    a = calorie_list[i]
    b = calorie_list[c]
    calorie_list_3[i]=b
    calorie_list_3[c]=a
    c = c-1 

#Output
print(calorie_list_1)
print(calorie_list_2)
print(calorie_list_3)

if(calorie_list_1==calorie_list_2==calorie_list_3):
    print("All three reversed lists are equal")
