'''
Q1. Check String are palendrome or not

def palendrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print("palendrome")
    else:
        print(" not palendrome")

palendrome("NAMAN")

--------------------------------------------------------------------------------------------------------------------------------------------------

'''