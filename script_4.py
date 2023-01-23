x = True
newNum = 0

while x == True:
    try:
        print("enter int #1: ",end="")
        in1 = int(input())
        newNum += in1
        x = False
    except ValueError:
        print("Invalid Input: please enter an int")

x = True

while x == True:
    try:
        print("enter int #2: ",end="")
        in1 = int(input())
        newNum += in1
        x = False
    except ValueError:
        print("Invalid Input: please enter an int")

x = True

while x == True:
    try:
        print("enter int #3: ",end="")
        in1 = int(input())
        newNum += in1
        x = False
    except ValueError:
        print("Invalid Input: please enter an int")

x = True

while x == True:
    try:
        print("enter int #4: ",end="")
        in1 = int(input())
        newNum += in1
        x = False
    except ValueError:
        print("Invalid Input: please enter an int")

x = True

while x == True:
    try:
        print("enter int #5: ",end="")
        in1 = int(input())
        newNum += in1
        x = False
    except ValueError:
        print("Invalid Input: please enter an int")

x = True

print("your sum is: ",newNum,end="")