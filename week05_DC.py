# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:20:58 2019

@author: Lu Haoyi
"""

# 50. Pow(x, n)
'''
Runtime: 16 ms, faster than 85.78% of Python online submissions for Pow(x, n).
Memory Usage: 11.8 MB, less than 45.87% of Python online submissions for Pow(x, n).
'''
def myPow(self, x, n):
    if n < 0:
        return 1 / self.myPowRecur(x, -n)
    else:
        return self.myPowRecur(x, n)
    
def myPowRecur(self, x, n):
    # Base case.
    if n == 0:
        return 1
    
    if n % 2 == 0:
        return self.myPowRecur(x * x, int(n / 2))
    else:
        return x * self.myPowRecur(x * x, int(n / 2))


# 14. Longest Common Prefix
'''
Runtime: 24 ms, faster than 63.38% of Python online submissions for Longest Common Prefix.
Memory Usage: 11.9 MB, less than 55.70% of Python online submissions for Longest Common Prefix.
'''
def longestCommonPrefix(self, strs):
    if not strs:
        return ''
    return self.helper(strs, 0, len(strs) - 1)
    
def helper(self, strs, left, right):
    if left == right:
        return strs[left]
    mid = left + (right - left)//2
    L = self.helper(strs, left, mid)
    R = self.helper(strs, mid + 1, right)
    # bianry search
    maxlength = max(len(L), len(R))
    i, j = 0, maxlength
    while i < j:
        m = i + (j - i)//2
        if L[i:m + 1] == R[i:m + 1]:
            i = m + 1
        else:
            j = m
    return R[:i]


# 23. Merge k Sorted Lists
'''
Runtime: 152 ms, faster than 32.82% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 19.9 MB, less than 36.57% of Python online submissions for Merge k Sorted Lists.
'''
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def mergeKLists(self, lists):
    if not lists:
        return None
    return self.helper(lists, 0, len(lists) - 1)
    

def helper(self, lists, left, right):
    if left == right:
        return lists[left]
    mid = left + (right - left)//2
    head1 = self.helper(lists, left, mid)
    head2 = self.helper(lists, mid + 1, right)
    dummy = ListNode(0)
    temp = dummy
    while (head1 and head2):
        if head1.val <= head2.val:
            temp.next = ListNode(head1.val)
            head1 = head1.next
        else:
            temp.next = ListNode(head2.val)
            head2 = head2.next
        temp = temp.next
    if head1:
        temp.next = head1
    if head2:
        temp.next = head2
    return dummy.next


# 4. Median of Two Sorted Arrays
# 没做出来，参考了discussion= =
def findMedianSortedArrays(self, nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 > len2:
        nums1, nums2 = nums2, nums1
        len1, len2 = len2, len1
    nums1 += [float('inf'), -float('inf')]
    nums2 += [float('inf'), -float('inf')]
    left = 0
    right = len1
    i = len1
    j = (len1 + len2) // 2 - i
    while max(nums1[i-1], nums2[j-1]) > min(nums1[i], nums2[j]):
        if nums1[i-1] > nums2[j]:
            right = i - 1
        else:
            left = i + 1
        i = (left + right) // 2
        j = (len1+ len2) // 2 - i
    if (len1 + len2) % 2 == 0:
        return (max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2.0
    return min(nums1[i], nums2[j])


































