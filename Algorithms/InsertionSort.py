'''
Insertion Sort Algorithm
Author: Ekramul Islam

Time Complexity: O(n^2) Best Case, Worst Case
Space Complexity: O(1) due to in-place sorting

Invariants: 1. The subarray arr[0..i-1] contains the i smallest elements of arr in sorted order
            2. The subarray arr[i..n-1] contains the n-i largest elements of arr in sorted order

What it does: 1. Find the minimum element in the unsorted array
              2. Swap the minimum element with the first element of the unsorted array
              3. Repeat the above steps for the remaining unsorted array


Stable: Yes
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted into the sorted portion
        j = i - 1  # Pointer to the previous element
        
        # Move elements of arr[0:i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key

# Example usage
# arr = [12, 11, 13, 5, 6]
# insertion_sort(arr)
# print("Sorted array:", arr)
