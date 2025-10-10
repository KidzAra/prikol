countsList = list(range(1,1000))

def listFiltrer(listToFilter):
    finalList = []
    for i in listToFilter:
        if i % 10 != 3 and i % 10 != 8:
            finalList.append(i)
    return finalList

print(listFiltrer(countsList))