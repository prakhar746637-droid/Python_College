'''
-> Types of methode in list
print(dir(list))

--------------------------------------------------------------------------------------------------------------------------------------------------

-> ye methode kya karte hai

help(list)

--------------------------------------------------------------------------------------------------------------------------------------------------

Q1. Print positive and negative elements of an List?


l = [-45,54,1214,-5,8,3]

print("Positive elements are")
for i in l:
    if i >= 0:
        print(i)

print("Negative elements are")
for i in l:
    if i <= 0:
        print(i)

------------------------------------------------------------------------------------------------------------------------------------------------

Q2. Mean of List elements?

l = [-45,54,1214,-5,8,3]
sum = 0
for i in l:
    sum = sum + i

print(sum/len(l))

--------------------------------------------------------------------------------------------------------------------------------------------------

Q3. Find the greatest element and print its index too?


l = [45,54,1214,5,8,3]

largest = l[0]
index = 0
for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i
print(f"Your largest number is {largest} and ther index is {i}")

-------------------------------------------------------------------------------------------------------------------------------------------------

Q4. Find the second greatest element?

l = [45,54,1214,5,8,3]

largest = l[0]
secLargest = l[0]
for i in l:
    if i > largest:
        secLargest = largest
        largest = i
    elif secLargest < i:
        secLargest = i

print(f"Your largest number is {secLargest}")

------------------------------------------------------------------------------------------------------------------------------------------------
Q5 Check if List is sorted or not.

'''
l = [45,54,1214,5,8,3]

for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else:
        print("List is not shorted")
        break

else:
    print("Your list is shorted")