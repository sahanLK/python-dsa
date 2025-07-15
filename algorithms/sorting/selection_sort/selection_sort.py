

def selection_sort(array: list):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        if i != min_index:
            array[min_index], array[i] = array[i], array[min_index]
    return array


list_to_sort = [4, 2, 6, 5, 1, 3]
print(selection_sort(list_to_sort))
