def bubblesort(array):
    temp = 0
    for i in range(len(array)-1):  # Cycles
        for j in range(0, len(array)-i-1):  # Elements compare
            if array[j] > array[j+1]:  # swapping
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


a = [5, 3, 1, 8, 4, 9, 7, 10, 2, 6]
b = bubblesort(a)
print(b)
