def maximumUnits(boxTypes, truckSize):
    """
    :type boxTypes: List[List[int]]
    :type truckSize: int
    :rtype: int
    """
    tot = 0
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    print('boxTypes: ', boxTypes)
    for box in boxTypes:
        if box[0] <= truckSize:
            tot += box[0] * box[1]
            truckSize -= box[0]
        else:
            tot += box[1] * truckSize
            break
    return tot


print(maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
