
def bubble_sort(array: list):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j+1] = temp
    return array


list_to_sort = [4, 3, 5, 1, 2]
print(bubble_sort(list_to_sort))
