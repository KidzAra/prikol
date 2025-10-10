countsList = list(range(1,1000))

#def listFiltrer(listToFilter):
#    finalList = []
#    for i in listToFilter:
#        if i % 10 != 3 and i % 10 != 8:
#            finalList.append(i)
#    return finalList

def listFiltrer(listToFilter):
    filteredList = []
    for i in listToFilter:
        if '3' not in str(i) and '8' not in str(i):
            filteredList.append(i)
    return filteredList

print(listFiltrer(countsList))