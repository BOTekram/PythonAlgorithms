'''
Selection Sorting Algorithm
Author: Ekramul Islam
'''

def selection_sort(arr): 
    '''
    Selection Sort Algorithm
    Time Complexity: O(n^2) Best Case, Worst Case 
    Space Complexity: O(1) due to in-place sorting

    Invariants: 1. The subarray arr[0..i-1] contains the i smallest elements of arr in sorted order
                2. The subarray arr[i..n-1] contains the n-i largest elements of arr in sorted order
    
    What it does: 1. Find the minimum element in the unsorted array
                  2. Swap the minimum element with the first element of the unsorted array
                  3. Repeat the above steps for the remaining unsorted array

    Stable: No
    '''
    n = len(arr)
    for i in range(n - 1): # Iterate through the array
        min_index = i
        for j in range(i + 1, n): # Find the minimum element in the unsorted array
            if arr[j] < arr[min_index]: # If the current element is smaller than the minimum element
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the minimum element with the current element

# Example usage
# input_list = [4, 2, 7, 1, 5, 3]
# selection_sort(input_list)
# print("Sorted list:", input_list)


