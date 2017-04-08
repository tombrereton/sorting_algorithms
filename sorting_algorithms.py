"""Unit test for algorithms"""
import unittest


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


class SortingTests(unittest.TestCase):
    a = []
    b = []

    def setUp(self):
        self.a = [4, 23, 3, 2, 23, 67, 34]
        self.b = [2, 3, 4, 23, 23, 34, 67]

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


if __name__ == '__main__':
    unittest.main()
