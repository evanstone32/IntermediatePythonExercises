def get_combined_dict(dict1,dict2):
    newDict ={}
    y = 0

    for i in dict1:
        for x in dict2:
            if i == x:
                newDict[i] = dict1[i] + dict2[x]
    
    return newDict
            




my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
