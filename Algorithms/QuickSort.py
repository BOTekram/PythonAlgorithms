'''
QuickSort Algorithm
Author: Ekramul Islam
'''

def quick_sort(arr):
    '''
    QuickSort Algorithm
    
    TimeComplexity best case: O(n log n) when the pivot is the middle element
    TimeComplexity worst case: O(n^2) because of the recursion
    SpaceComplexity: O(n) because of the recursion

    Invariants: 1. The subarray arr[0..i-1] contains the i smallest elements of arr in sorted order
                2. The subarray arr[i..n-1] contains the n-i largest elements of arr in sorted order

    What it does: 1. Choose a pivot
                  2. Partition the array into two subarrays such that all elements in the left subarray are less than or equal to the pivot and all elements in the right subarray are greater than the pivot
                  3. Recursively apply the above steps to the left subarray and the right subarray

    Stable: No
    '''
    if len(arr) <= 1: # Base case
        return arr
    
    pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
    left = [x for x in arr if x < pivot] # Elements less than pivot
    middle = [x for x in arr if x == pivot] # Elements equal to pivot
    right = [x for x in arr if x > pivot] # Elements greater than pivot
    
    return quick_sort(left) + middle + quick_sort(right) # Recursively apply the above steps to the left subarray and the right subarray

# Example usage
# unsorted_list = [3, 6, 8, 10, 1, 2, 1]
unsorted_list = [9,6,5,3,1,2,4,7,8]
sorted_list = quick_sort(unsorted_list)
print(sorted_list)
