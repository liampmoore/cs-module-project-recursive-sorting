# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # we have an array of zeroes to overwrite equaling the length of both arrays
    # Your code here

    # keep track of merged_arr index
    merged_index = 0
    # keep track of array A index
    a_index = 0
    # keep track of array B index
    b_index = 0
    # while the merged index is less than number of elements - 1
    while merged_index < elements:
        # if A still has items and (B has no items or the current item of array A is less than the current B)
        if a_index < len(arrA) and (b_index == len(arrB) or arrA[a_index] < arrB[b_index]):
            # add item A to merged_arr current index
            merged_arr[merged_index] = arrA[a_index]
            # increment a_index
            a_index += 1
            # increment merged_arr current index
            merged_index += 1
        else:
            # add item B to merged_arr current index
            merged_arr[merged_index] = arrB[b_index]
            # increment b_index
            b_index += 1
            # increment merged_arr current index
            merged_index += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    
    # if you can break it down further
    if len(arr) > 1:
        # break the array down into two smaller arrays and call merge sort on each
        middle = len(arr) // 2
        arrA = merge_sort(arr[:middle])
        arrB = merge_sort(arr[middle:])
        arr = merge(arrA, arrB)
        # call merge on the two arrays
    else:
        return arr

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
