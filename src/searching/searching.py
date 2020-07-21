# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if len(arr) == 0:
        return -1

    if start == end:
        return -1

    # find the middle of the start and the end
    middle = (start + end) // 2
    # if the middle is the target return the middle
    if arr[middle] == target:
        return middle
    # elif the target is less than the middle call binary search again on the lower half
    elif target < arr[middle]:
        return binary_search(arr, target, start, middle)
    # else call binary search on the higher half
    else:
        return binary_search(arr, target, middle + 1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
