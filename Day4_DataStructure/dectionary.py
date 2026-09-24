'''
Q1. Write a Python script to merge two Python dictionaries?

d1 = {10:200, 20:300, 30:400, 40:500}
d2 = {50:600, 60:700, 70:800, 80:900}

for i in d2:
    d1[i] = d2[i]

print(d1)

------------------------------------------------------------------------------------------------------------------------------------------------

Q2. Write a Python program to sum all the values in a dictionary?

d1 = {10:200, 20:300, 30:400, 40:500}

sum = 0

for i in d1:
    sum = sum + d1[i]

print(sum)

----------------------------------------------------------------------------------------------------------------------------------------------------

Q3. Count the frequency of each element in a list

a = [1,1,1,12,2,2,2,24,4,5,6,6,6]

d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)

-------------------------------------------------------------------------------------------------------------------------------------------------

Q4. Write a Python program to combine two dictionary by adding
    values for common keys.

'''
d1 = {10:200, 20:300, 30:400, 40:500}
d2 = {40:600, 60:700, 70:800, 80:900}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]