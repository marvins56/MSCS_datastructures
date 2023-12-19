# Iterative Binary Search Function
# It prints the index of x in given array arr if present,
# else prints that the element is not present
arr = [2, 3, 4, 10, 40, 50, 51, 60, 1]

def binary_search(arr):
    print(f"enter number to search in the array: {arr}")
    x= int(input())

    low = 0
    high = len(arr) - 1
    # [1,5,6,7]
    while low <= high:
        mid = (high + low) // 2 
        # looking for the pivot

        # Check if x is present at mid
        if arr[mid] == x:
            print("Element is present at index", mid)
            return

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, the element was not present
    print("Element is not present in array")

# Function call
binary_search(arr)
