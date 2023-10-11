'''
Binary Search Algorithm
Author: Ekramul Islam
'''

def BinarySearch (arr, l, r, x):
    '''
    arr = sorted array
    l = left index
    r = right index
    x = element to be searched

    Time Complexity: O(log n) Best Case, Worst Case
    Space Complexity: O(1) due to in-place sorting

    Invariants: 1. The subarray arr[0..i-1] contains the i smallest elements of arr in sorted order
                2. The subarray arr[i..n-1] contains the n-i largest elements of arr in sorted order
    
    What it does: 1. Find the minimum element in the unsorted array
                  2. Swap the minimum element with the first element of the unsorted array
                  3. Repeat the above steps for the remaining unsorted array

    Stable: No
    '''
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BinarySearch(arr, l, mid - 1, x)
        else:
            return BinarySearch(arr, mid + 1, r, x)
    else:
        return -1