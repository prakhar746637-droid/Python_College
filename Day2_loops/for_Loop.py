'''
a = 'nature'
for i in range(len(a)):
    print(a[i])

--------------------------------------------------

Q1 - Accept an integer and Print hello Prakhar n times


n = int(input('Enter a number'))
for i in range(1,n+1,1):
    print("Hello Prakhar")

----------------------------------------------------------

Q2 Print natural number up to n

n = int(input('Enter a number :->'))
for i in range(1,n+1,1):
    print(i)

--------------------------------------------------------------

Q3. Reverse for loop. Print n to 1

n = int(input('Enter a number :-> '))
for i in range(n,0,-1):
    print(i) 

------------------------------------------------------------------------

Q4 Take a number as input and print its table

n = int(input('Enter a number :->'))
for i in range(1,11,1):
    print(f"{n} X {i} = {n*i}")

----------------------------------------------------------------------------

Q5 - Sum up to n terms

n = int(input('Enter a number :->'))
sum = 0
for i in range(1,n+1,1):
    sum = sum + i
print(f"Sum of number is from 1 to {n} :-> {sum}")

----------------------------------------------------------------------------

Q6 Factorial of a number

n = int(input('Enter a number :->'))
fact = 1
for i in range(1,n+1,1):
    fact = fact*i
print(f"factorial of number of {n} :-> {fact}")

--------------------------------------------------------------------------------

Q7. Print the sum of all even & odd numbers in a range
separately


n = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print(f"Sum of Even numbers from 1 to {n} => {even_sum}")
print(f"Sum of Odd numbers from 1 to {n} => {odd_sum}")

----------------------------------------------------------------------------

Q8. print all factor of a numbrer

n = int(input("Enter a number :-> "))
for i in range(1, n+1, 1):
    if n%i ==0:
        print(f"factorial of number {n} :=> {i}")

---------------------------------------------------------------------------------------
        
Q8 Accept a number and check if it a perfect number or not.
A number whose sum of factors is equal to the number itself
Ex - 6 = 1, 2, 3 =6


n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print(f"Number {n} is a perfect number")
else:
    print(f"Number {n} is not a perfect number")

---------------------------------------------------------------------------------------------

Q9 - Check wether the number is prime or not


n = int(input("Enter a number: "))
count = 0
for i in range(1,n+1,1):
    if n%i ==0:
        count +=1
if count == 2:
    print(f"Number {n} is prime number")
else:
    print(f"Number {n} is not prime number")

-----------------------------------------------------------------------------------------------------

Q10 - Reverse a string without using in build functions

     1st Method

a = "Prakhar Mishra"
print(a[::-1])

     2nd method

a = "Prakhar Mishra"
for i in range(len(a)-1,-1,-1):
    print(a[i])

-----------------------------------------------------------------------------------
Q11 - Check string is Pallindrome or not

a = 'naman'
b= ''
for i in range(len(a)-1,-1,-1):
    b = b + a[i]

if b ==a:
    print("Your string are palendrome")
else:
    print("Your string are not palendrome")

-----------------------------------------------------------------------------------

Q12. Count all letters digits and special symbol from a given string

'''
a = "afh@$#%78876"
char = 0
dig =0
spchar = 0
for i in a:
    if i.isdigit():
        dig +=1
    elif i.isalpha():
        char += 1
    else:
        spchar =+ 1
print(f"Digits => {dig}")
print(f"charecter => {char}")
print(f"special charecter => {spchar}")