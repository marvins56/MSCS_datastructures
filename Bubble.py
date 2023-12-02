# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n-1):
        # Initialize swapped to False at the beginning of each outer loop iteration
        swapped = False

        # Traverse the array from 0 to n-i-1
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
         
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
 
# Driver code to test above
arr = [64, 34, 1, 25, 12, 22, 11, 90, 0]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
