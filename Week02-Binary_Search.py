# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:30:48 2019

@author: Haoyi Lu
"""

# 69. Sqrt(x)

'''
Runtime: 16 ms, faster than 98.01% of Python online submissions for Sqrt(x).
Memory Usage: 11.6 MB, less than 84.54% of Python online submissions for Sqrt(x).
'''

def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    l, r = 0, x
    while l < r:
        mid = l + (r-l)//2
        if mid ** 2 <= x < (mid + 1)**2:
            return mid
        if mid**2 < x:
            l = mid + 1
        else:
            r = mid
    return l



# 852. Peak Index in a Mountain Array
'''
Runtime: 60 ms, faster than 73.00% of Python online submissions for Peak Index in a Mountain Array.
Memory Usage: 12.8 MB, less than 27.12% of Python online submissions for Peak Index in a Mountain Array.
'''

def peakIndexInMountainArray(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    l, r = 0, len(A) - 1
    while l + 1 < r:
        mid = l + (r-l)//2
        if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
            return mid
        if A[mid] > A[mid + 1]:
            r = mid
        else:
            l = mid
    if A[r] > A[l]:
        return r
    else:
        return l
    

# 74. Search a 2D Matrix
'''
Runtime: 56 ms, faster than 55.47% of Python online submissions for Search a 2D Matrix.
Memory Usage: 13.6 MB, less than 48.74% of Python online submissions for Search a 2D Matrix.
'''

def searchMatrix(self, matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    l, r = 0, len(matrix)*len(matrix[0])

    while l<r:
        mid = (l+r)//2
        low, high = mid//len(matrix[0]), mid%len(matrix[0])
        if matrix[low][high]==target:
            return True
        elif matrix[low][high]>target:
            r = mid
        else:
            l = mid + 1

    return False

# 34. Find First and Last Position of Element in Sorted Array
'''
Runtime: 68 ms, faster than 76.47% of Python online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 13.1 MB, less than 36.91% of Python online submissions for Find First and Last Position of Element in Sorted Array.
'''

def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    

    # find the left index
    if(len(nums) == 0):
        return [-1,-1]
    
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + ((right - left)>>1)
        if (nums[mid] < target):
            left = mid + 1
        else:
            right = mid
    if nums[left] != target:
        return [-1, -1]
    # find right index
    l = left
    r = len(nums) - 1
    while l < r:
        m = l + ((r-l)>>1)
        if(nums[m] > target):
            r = m - 1
        else:
            l = m + 1
    if nums[r] != target:
        return [left, r-1]
    else:
        return [left,r]
    
# 240. Search a 2D Matrix II
'''
Runtime: 100 ms, faster than 35.64% of Python online submissions for Search a 2D Matrix II.
Memory Usage: 15.7 MB, less than 74.93% of Python online submissions for Search a 2D Matrix II.
'''
def searchMatrix2(self, matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    
    row = len(matrix) - 1
    while row >= 0:
        if matrix[row][0] == target:
            return True
        elif matrix[row][0] > target:
            row -= 1
        else:
            l, r = 0, len(matrix[0])
            while l < r:
                mid = l + (r-l)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid
            row -= 1
    return False
