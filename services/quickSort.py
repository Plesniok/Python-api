def quickSort(reqList):
    if len(reqList) <= 1:
        return reqList
    pivot = reqList[len(reqList) - 1]
    pivotList = []
    lowerList = []
    higherList = []
    for number in reqList:
        if number < pivot:
            lowerList.append(number)
        elif number > pivot:
            higherList.append(number)
        elif number == pivot:
            pivotList.append(number)
    resList = []
    print("__________")
    print(lowerList)
    print(pivot)
    print(higherList)
    print(pivotList)
    print("__________")

    resList.extend(quickSort(lowerList))
    resList.append(pivot)
    resList.extend(pivotList[0:len(pivotList) - 1])
    resList.extend(quickSort(higherList))
    return resList
    
