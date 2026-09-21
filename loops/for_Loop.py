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


'''
n = int(input("Enter a number :-> "))

