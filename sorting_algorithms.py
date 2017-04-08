import unittest
import random

"""
This is an implementation of common sorting algorithms.
The algorithms are based on the implementations found
on the geeksforgeeks website.
The algorithms are unit tested to ensure correctness.
"""


def selectionSort(a):
    for i in range(len(a) - 1):

        # find index of min element
        min_index = i
        for j in range(i + 1, len(a)):
            if (a[j] < a[min_index]):
                min_index = j

        # swap ith element with min element
        temp = a[i]
        a[i] = a[min_index]
        a[min_index] = temp
    return a


def insertionSort(a):
    """
    a[m + 1..r] is the unsorted portion
    a[l...m] is the sorted portion
    a[l...m] is initialised with the left most element which is sorted.
     we take the left most item in the unsorted portion.
     We insert the item into the sorted portion so
     that it remains sorted.
    :param a:
    :return:
    """
    for i in range(1, len(a)):
        temp = a[i]
        j = i
        while (j > 0 and temp < a[j - 1]):
            a[j] = a[j - 1]
            j -= 1
        a[j] = temp
    return a


def merge(arr, left, mid, right):
    """
    Merges 2 sub array of arr[l...r]
    First sub array is arr[l...m]
    Second sub array is arr[m+1...r]
    """

    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays
    left_array = [0] * (n1)
    right_array = [0] * (n2)

    # copy data to temp arrays left_array[], right_array[]
    for i in range(0, n1):
        left_array[i] = arr[left + i]

    for j in range(0, n2):
        right_array[j] = arr[mid + 1 + j]

    # merge the temp arrays back into arr[l...r]
    i = 0  # initial index of left sub array
    j = 0  # initial index of right sub array
    k = left  # initial index of merged subarray

    while i < n1 and j < n2:
        if (left_array[i] <= right_array[j]):
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    # Copy the remaining elements of left_array[], if there
    # are any
    while (i < n1):
        arr[k] = left_array[i]
        i += 1
        k += 1

    # Copy the remaining elements of right_array[], if there
    # are any
    while (j < n2):
        arr[k] = right_array[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    """

    :param arr: array to be sorted
    :param left: the left index of the sub array to be sorted
    :param right: the right index of the sub array to be sorted
    :return:
    """
    if (left < right):
        # same as (l+r)/2, but avoids overflow for large l and r
        mid = int((left + (right - 1)) / 2)

        # Sort first and second halves
        # We do this by reducing left and right until we have
        # a difference of 1 (ie array length is 1)
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def partition(arr, low, high):
    """
    This function takes middles element as pivot.
    It then places the pivot in its correct position so
    that elements smaller than the pivot are to its left,
    bigger elements to the right.
    :param arr:
    :param low:
    :param high:
    """

    # get random index between and including low and high
    random_index = random.randint(low, high)
    pivot = arr[random_index]  # pivot

    # swap pivot and rightmost entry
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # get left and right 'fence posts'
    leftpost = low
    rightpost = high - 1

    # left of leftpost is 'less' than pivot
    # right of rightpost is 'more' than pivot
    # 1. move leftpost as far as possible
    # 2. move rightpsot as far as possible
    # 3. swap 2 entries & move both posts in
    # repeat 1 to 3
    # stop when leftpost and rightpost coincide
    while (leftpost <= rightpost):
        while (leftpost <= rightpost and arr[leftpost] <= pivot):
            leftpost += 1
        while (leftpost <= rightpost and arr[rightpost] >= pivot):
            rightpost -= 1
        if (leftpost < rightpost):
            # we are at step 3, therefore swap entries
            arr[leftpost], arr[rightpost] = arr[rightpost], arr[leftpost]
    # we put pivot back in where leftpost is
    arr[leftpost], arr[high] = arr[high], arr[leftpost]
    return (leftpost)


def quickSort(arr, low, high):
    """
    :param arr: The array to be sorted
    :param low: starting index
    :param high: ending index
    :return:
    """
    if (low < high):
        # pi is partitioning index
        pi = partition(arr, low, high)

        # separately sort elements that are less than
        # partition, and elements greater than partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def countingSort(a, exp1):
    """
    A function to do counting osrt of a[] according to the
    digit represent by exp1
    :param a:
    :param exp1:
    :return:
    """

    n = len(a)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # Initialise count array as 0
    count = [0] * (10)

    # Store count of occurances in count[]
    for i in range(0, n):
        index = int(a[i] / exp1)
        count[(index) % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # postion of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while (i >= 0):
        index = int(a[i] / exp1)
        output[count[(index) % 10] - 1] = a[i]
        count[(index) % 10] -= 1
        i -= 1

    # Copying the output array to a[]
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(a)):
        a[i] = output[i]


def radixSort(a):
    """
    Radix sort
    :param a: array to be sorted
    """

    # Find the maximum number to know number of digits
    max1 = max(a)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while (max1 / exp > 0):
        countingSort(a, exp)
        exp *= 10


class SortingTests(unittest.TestCase):
    a = []
    b = []
    c = []
    d = []

    def setUp(self):
        self.a = [4, 23, 3, 2, 23, 67, 34]
        self.b = [2, 3, 4, 23, 23, 34, 67]
        self.c = [10, 7, 5, 1, 3, 2]
        self.d = [1, 2, 3, 5, 7, 10]

    def test_SelectionSort(self):
        """selection sort test"""
        result = selectionSort(self.a)
        self.assertEqual(result, self.b)

    def test_InsertionSort2(self):
        """insertion sort 2 test"""
        result = insertionSort(self.a)
        self.assertEqual(result, self.b)

    def test_MergeSort(self):
        """merge sort test"""
        mergeSort(self.a, 0, len(self.a) - 1)
        self.assertEqual(self.a, self.b)

    def test1_quicksort(self):
        """quick sort test"""
        quickSort(self.c, 0, len(self.c) - 1)
        self.assertEqual(self.c, self.d)

    def test2_quicksort(self):
        """quick sort test 2"""
        quickSort(self.a, 0, len(self.a) - 1)
        self.assertEqual(self.a, self.b)

    def test_radixSort(self):
        """radix sort test"""
        radixSort(self.a)
        self.assertEqual(self.a, self.b)


if __name__ == '__main__':
    unittest.main()
