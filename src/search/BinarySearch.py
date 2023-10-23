# recursive approach for binary search
def binary_search(arr, low, high, x):
    # check base case
    if high >= low:
        mid = (high+low)//2

        # if the element is present in the pointer (mid)
        if(arr[mid]) == x:
            return mid
        # the element can only be present in the left
        elif arr[mid] > x:
            return binary_search(arr, low, mid -1, x)
        # the element can only be present in the right
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        # return -1 when the element is not found in the array
        return -1

## Testing
arr = [2, 3, 4, 10, 30, 100]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print("Result found at index", str(result))
else:
    print("Number not found")
