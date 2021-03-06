# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    mid = int((start + end) / 2)
    if start >= end:
        return -1
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid, end)
    else:
        return binary_search(arr, target, start, mid)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
