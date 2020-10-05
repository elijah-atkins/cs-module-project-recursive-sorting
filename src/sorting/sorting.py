# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    #index pointers
    arrA_index = 0
    arrB_index = 0
    merged_index = 0
    #check that arrays are not empty
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[merged_index] = arrA[arrA_index]
            arrA_index += 1
        else:
            merged_arr[merged_index] = arrB[arrB_index]
            arrB_index += 1
        merged_index +=1
    
    #loop through any remaining elements
    while arrA_index < len(arrA):
        merged_arr[merged_index] = arrA[arrA_index]
        arrA_index += 1
        merged_index += 1
    
    while arrB_index < len(arrB):
        merged_arr[merged_index] = arrB[arrB_index]
        arrB_index += 1
        merged_index += 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        middle = (len(arr) // 2)
        left_arr = merge_sort(arr[:middle])
        right_arr = merge_sort(arr[middle:])

        return merge(left_arr, right_arr)

    return arr
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

