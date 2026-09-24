from pathlib import Path

def readfileandfolder():
    path = Path('')                     # curunt file ka path blank string ke andar aa jayega
    items = list(path.rglob('*'))       # path ke andar ke sare function read karne ke liye recursive glob function (rglob) ka use karte hai
    for i, items in enumerate(items):   # intex (i) & value (items) ko alag alag save karne ke liye enumerate ka use karte hai
        print(f"{i+1} : {items}")

def createFile():
    try:
        readfileandfolder()
        name = input("tell your file name :-> ")
        p = Path(name)                       # name vali file ko path mein include kare ke liye
        if not p.exists():
            with open(p,"w") as fs:
                data = input("What you want to write in this file :-> ")
                fs.write(data)
            print("file created Successfully")
        else :
            print("This file already exist")
    except Exception as err:
        print(f"An error occured as {err}")

def readFile():
    try:
        readfileandfolder()
        name = input("Which file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("readed file succesfully")
        else:
            print("file does not exist")

    except Exception as err:
        print(f"An error occured as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("Tell your response :- "))

if check == 1:
   createFile()

if check == 2:
    readFile()


# 7:11