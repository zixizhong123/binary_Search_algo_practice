"""
Program name: Find the floor value in a Sorted Array (Binary search)
Description: Given a sorted array arr[] of size N without duplicates, and given a value x.
                Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x.
                Find the index of K(0-based indexing).

source: https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array

"""
import random
import math


class Solution:

    def findFloor(self, arr, n, key):
        '''
            This method returns the index of the required value
            using binary search algorithm
            Parameters: self
                        arr - the searching array
                        n - the size of the array
                        key - the searching value
            Returns: result
        '''
        result = -1
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (hi - lo) // 2 + lo

            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                if result == -1 or arr[mid] > arr[result]:
                    result = mid
                lo = mid + 1
            else:
                # When arr[mid] > key
                hi = mid - 1
        return result

    """
    This is a function that allows you to generate a huge sorted list with random values
    if you would like to test the program against a really large array
    """
    # def bigarr(n):
    #     result = [1]
    #     a = 0
    #     b = 10
    #     while len(result) < n:
    #         num = random.randint(a, b)
    #         result.append(num)
    #         a = a + b
    #         b = b * 2
    #     return result


def main():
    T = int(input("Enter how many tests you would like to do?"))
    while (T > 0):
        size = int(input("Please define size of the array in your test plan: "))
        key = int(input("Please enter the key you would like to search: "))
        arr = [int(x) for x in input("Please enter the elements in your list(seperated by comma): ").strip().split(",")]
        obj = Solution()
        pos = obj.findFloor(arr, size, key)
        if pos == -1:
            print("the value is not found")
        else:
            print(f"the value is : {arr[pos]}, index is :{pos}")

        T-= 1


main()
