def adjacentElementsProduct(inputArray):
    products = list()
    for i in range(0,len(inputArray)-1):
        print inputArray[i] * inputArray[i+1]
        products.insert(i,inputArray[i] * inputArray[i+1])
    products = sorted(products)
    print products
    lastElement = products[-1]
    return lastElement

inputArray = [3, 6, -2, -5, 7, 3]

print adjacentElementsProduct(inputArray)