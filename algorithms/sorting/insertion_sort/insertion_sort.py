
def insertion_sort(array: list):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1

        while temp < array[j] and j > -1:
            array[j + 1] = array[j]
            array[j] = temp
            j -= 1
    return array


list_to_sort = [4, 3, 5, 1, 2]
print(insertion_sort(list_to_sort))


