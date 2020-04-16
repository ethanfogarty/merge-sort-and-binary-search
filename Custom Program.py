from random import randint


# Builds a list of x numbers randomly from n', to n
def list_setup():
    for i in range(10):
        custom_list.append(randint(1, 10))
    merge_sort(custom_list)


# Uses the merge sort algorithm on the previously built list
def merge_sort(sorted_list):
    if len(sorted_list) == 1:
        return sorted_list
    else:
        mid = len(sorted_list) // 2
        left = sorted_list[:mid]
        right = sorted_list[mid:]

        merge_sort(left)
        merge_sort(right)

# Part of the function that sorts and merges the lists back together
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list[k] = left[i]
            i += 1
        else:
            sorted_list[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        sorted_list[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(left):
        sorted_list[k] = right[j]
        j += 1
        k += 1
    # Makes the sorted list available across the program in a global variable
    globals()['sorted_list'] = sorted_list


# Performs a binary search on the list that has been created and sorted
def binary_search(arr, n):
    lower = 0
    upper = len(arr) - 1
    while lower <= upper:
        # // gives you int division
        mid = (lower + upper) // 2
        if arr[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if arr[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1
    return False


# Initializes the list that will be used throughout the program
custom_list = []

# Initializes sorted list global variable
sorted_list = []

# Initializes the starting function
list_setup()

# Initializes the position global variable to allow printing of the index of the searched number
pos = 0

# Takes in the number desired to be binary searched
n = input("Enter a number to be searched. ")
if binary_search(sorted_list, int(n)):
    print(sorted_list)
    print("Found at ", pos, " index")
else:
    print(sorted_list)
    print("Not Found")
