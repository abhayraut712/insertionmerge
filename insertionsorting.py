def insertionsort(arr):

    for i in range (1, len(arr)):
        currentnum = arr[i]
        j = i-1
        while j>=0 and currentnum < arr[j] :
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = currentnum
    return arr
