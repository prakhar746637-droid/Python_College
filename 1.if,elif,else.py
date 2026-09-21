"""
Q.1 Accept the number and print gretest of two number

Num1= int(input("Input first number"))
Num2= int(input("Input Secound number"))
if Num1 > Num2:
    print(f"{Num1} is greter then {Num2}")
elif Num2 > Num1 :
    print(f"{Num2} is greter then {Num1}")
else:
    print("both are numbers are same")

------------------------------------------------------------------------------------

Q2.  Accept the gender from user as char and print the respective greeting message

c1 = input("Enter your gender")

if c1 == "m":
    print(f"good morning sir You are male")
else:
    print(f"good morning mam You are female")

---------------------------------------------------------------------------------------------

Q3. Accept an integer to check whether it is an even number or odd

n = int(input("enter your number :-> "))
if n%2==0:
    print(f"Nuber {n} is even😊")
else :
    print(f"Number {n} is odd😒")

----------------------------------------------------------------------------------------------

Q4. Accept name and age from the User. check if the user is valid voter or not.

name = input("Enter your name :-> ")
age = int(input("enter your age :-> "))
if age < 0:
    print("Please input correct Age")
elif age < 18:
    print(f"You are not vailed voter becouse your age is {age}")
else :
    print(f"You are vailed voter becouse your age is {age}")

----------------------------------------------------------------------------------------------------- 

Q5. Accept a year  and check if it a leap year or not 

note :-> A leap year is the year where :
          century year deviseble by 400 and 100
          non century year is deviseble by 4
year = int(input("Enter year"))
if year%100 ==0 and year %400 == 0:
    print("Year is century year and a leap year")
elif year %100 !=0 and year%4 ==0:
    print("Year is leap year")
else :
    print("it is normal year")

---------------------------------------------------------------------------------------------------------

Q.6 If- elif ladder
    @ You cna also create if elif ladder using multiple conditions of
elif.j
@ For understanding solve this questionj
@ take the input of temperature in celsiusX
@ Below 0°C → "Freezing Cold b
@ 0°C to 10°C → "Very Cold b
@ 10°C to 20°C → "Cold b
@ 20°C to 30°C → "Pleasant b
@ 30°C to 40°C → "Hot b
@ Above 40°C → "Very Hot "


"""
t = int(input("Input temperature in celsius:-> "))
if t<=0:
    print("Freezing cold")
elif t>=0 and t<=10:
    print("Very cold")
elif t>=10 and t<=20:
    print("cold")
elif t>=20 and t<=30:
    print("Pleasant")
elif t>=30 and t<=40:
    print("hot")
else :
    print("Very hot")