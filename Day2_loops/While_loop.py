'''
Q1. Separate each digit of a number and print it on the new line

a=int(input("tell your number"))
while a>0:
    print(a%10)
    a = a//10

----------------------------------------------------------------------------------

Q2. Accept a number and print its reverse 
a=int(input("tell your number :-> "))
rev =0
while a>0:
    rev = rev*10 + a%10
    a = a//10
print(rev)

--------------------------------------------------------------------------------------------

Q3. Accept a number and check if it is a pallindromic number(sidha uulta same) (If
number and its reverse are equal?


a=int(input("tell your number :-> "))
copy = a
rev = 0
while a>0:
    rev = rev*10 + a%10
    a = a//10
if rev == copy:
    print("palandrom")
else:
    print("not palindrom")

----------------------------------------------------------------------------------------------

Q4. Create a random number guessing game with python.

'''
import random

num = random.randint(1, 10)

tries = 0

while True:
    guess = int(input("Please guess your number :-> "))

    if num == guess:
        tries += 1
        print(f"You are right with no of tries = {tries}")
        break

    elif num < guess:
        tries += 1
        print("Go a little lower")

    elif num > guess:
        tries += 1
        print("Go a little higher")
