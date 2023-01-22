def get_unique_list(myList):
    unList = myList[:]
    unList.insert(0,0)

    for i in unList:
        for x in unList:
            if (unList[i] == unList[x] and x != i):
                del unList[x]

    del unList[0]
    return unList


myList = [1,2,3,2,1,4]
uniqueList = get_unique_list(myList)
print(uniqueList)
            


