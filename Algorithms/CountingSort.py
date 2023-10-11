'''
Counting Sort Algorithm
Author: Ekramul Islam
'''

def countingSort(arr):
    '''
    Counting Sort Algorithm
    Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input, Best Case, Worst Case
    Space Complexity: O(n+k) due to count array

    Invariants: 1. The subarray arr[0..i-1] contains the i smallest elements of arr in sorted order
                2. The subarray arr[i..n-1] contains the n-i largest elements of arr in sorted order

    What it does: 1. Find the minimum element in the unsorted array
                  2. Swap the minimum element with the first element of the unsorted array
                  3. Repeat the above steps for the remaining unsorted array
    Stable: Yes

    '''
    size = len(arr)
    output = [0] * size
    # count array initialization
    count = [0] * 10
    # storing the count of each element 
    for m in range(0, size):
        count[arr[m]] += 1
    # storing the cumulative count of each array
    for m in range(1, 10):
        count[m] += count[m - 1]
    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1
    for m in range(0, size):
        arr[m] = output[m]

# Example usage
# data = [3, 5, 1, 6, 7, 8, 3]
# countingSort(data)
# print("Sorted Array: ")
# print(data)
