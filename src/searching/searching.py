def binary_search(arr, target, start, end):
    #end recursion if nothing is found
    if start > end:
        return -1
    #get the middle
    middle = (start + end) // 2
    if target is arr[middle]:
        return middle
    else:
        if target < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        #call recursion
        return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def decending_binary_search(arr, target, start, end):
    #end recursion if nothing is found
    if start > end:
        return -1
    #get the middle
    middle = (start + end) // 2
    if target is arr[middle]:
        return middle
    else:
        #target greater than arr item puts list in decending order
        if target > arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        return decending_binary_search(arr, target, start, end)

def agnostic_binary_search(arr, target):
    # Your code here
    array_length = len(arr) - 1
    if arr[0] < arr[array_length]:
        return binary_search(arr, target, 0, array_length)
    if arr[0] > arr[array_length]:
        return decending_binary_search(arr, target, 0, array_length)

