
def numWords(in1):
    word = in1.lower()
    newDict = {}

    #initializes new dict with the letters
    for i in word:
        if i in newDict:
            x =0
        else:
            newDict[i] = 0

    #counts the amount of letter in string
    for i in word:
        newDict[i] += 1

    return newDict

print("please enter a sting: ")
in1 = input()
print(numWords(in1))