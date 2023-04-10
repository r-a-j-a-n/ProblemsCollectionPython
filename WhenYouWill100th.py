from datetime import date

#Getting year 
year = date.today().year 

age_year = input("Enter the age or year of birth \n")


#Checking if input is string
try:
    CheckingInput = int(age_year)
except Exception as e :
    print("Age / Year of birth can't be in words")
    exit()

# Checking Different Invalid Input Cases
if len(age_year)>4:
    print("Invalid Input :: Age/Year of birth can't be more then 4 digits")
    exit()
elif int(age_year) == 0:
    print("You are just born . Go and have duddu")
    exit()

elif int(age_year)<0:
    print("Invalid Input :: Age /Year of birth can't be negative")
    exit()
elif int(age_year)>year:
    print("You are not born yet");
    exit()




if len(age_year)==4:
    # print("You have entered your year of birth")
    print("You will get 100 on",int(age_year)+100)
else:
    #Checking if the input age is valid or not
    if  int(age_year)>150:
        print("Invalid Input :: You are the oldest person ever existed")
        exit()
    # print("You have entered your age")
    birth_year = year - int(age_year)
    print("You will get 100 on",int(birth_year)+100)
    


