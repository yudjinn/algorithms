def gcd(a,b):
    """
    Finds and returns the greatest common denominator of two values.
    a,b -> inputs
    """
    while (b != 0):
        t = a
        a = b
        b = t % b

    return a

def bubbleSort(dataset):
    """
    Simple bubble sort, takes in a list of numbers and returns a sorted list
    """
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
        print(dataset)



def mergeSort(dataset):
    """
    In-place merge sort
    """
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        #Recursively break down the array
        mergeSort(leftarr)
        mergeSort(rightarr)

        #Perform meging
        i = 0 # index for left array
        j = 0 # index for right array
        k = 0 # index into merged array

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        #if left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        #if left array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


def quickSort(dataset, first, last):
    """
    In-place quick sort
    """
    if first < last:
        #calculate split point
        pivotIdx = partition(dataset, first, last)

        #now sort partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)

def partition(datavalues, first, last):
    """
    Supporting function for quickSort, returns split point
    """
    #select first item as pivot value
    pivotval = datavalues[first]

    #establish upper and lower indices
    lower = first + 1
    upper = last

    #start searching for crossing point
    done = False
    while not done:
        #advance lower index
        while lower <= upper and datavalues[lower] <= pivotval:
            lower += 1

        #advance upper index
        while upper >= lower and datavalues[upper] >= pivotval:
            upper -= 1

        #split point is when indices cross
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    #when the split point is found, exchange the pivot values
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    #return split point index
    return upper

def main():
    # print(gcd(60, 96)) # should be 12
    # print(gcd(20, 8)) #should be 4
    unsorted = [14,6,4,94,35,41,13,65,48,23]
    print(unsorted)
    # bubbleSort(unsorted)
    # mergeSort(unsorted)
    # quickSort(unsorted, 0, len(unsorted)-1)
    print(unsorted)

if __name__ == '__main__':
    main()
