'''
Radix Sort Algorithm 
Author: Ekramul Islam

Time Complexity: O(nk) where n is the number of elements in input array and k is the number of digits in the largest element, Best and worst case

Space Complexity: O(n+k) due to count array, where n is the number of elements in input array and k is the range of input

Invariants: 1. The subarray arr[0..i-1] contains the i smallest elements of arr in sorted order
            2. The subarray arr[i..n-1] contains the n-i largest elements of arr in sorted order

What it does: 1. Find the minimum element in the unsorted array
              2. Swap the minimum element with the first element of the unsorted array
              3. Repeat the above steps for the remaining unsorted array
             
Stable: Yes
'''

def counting_sort(arr, exp):
    '''
    Parameters
    ----------
    arr : TYPE
        DESCRIPTION.
    exp : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Update count array to contain actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    
    # Perform counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

#Example usage
# arr = [170, 45, 75, 90, 802, 24, 2, 66]
# radix_sort(arr)
# print("Sorted array:", arr)
