# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:06:24 2019

@author: Lu Haoyi
"""

# ------------------GROUP A--------------------------

# 784. Letter Case Permutation
'''
Runtime: 48 ms, faster than 67.73% of Python online submissions for Letter Case Permutation.
Memory Usage: 13.4 MB, less than 20.30% of Python online submissions for Letter Case Permutation.
'''
def letterCasePermutation(self, S):
    res, s = [], list(S)
    def bt(index):
        if index == len(s):
            res.append(''.join(s))
            return
        if s[index].isalpha():
            bt(index + 1)
            s[index] = chr(ord(s[index]) ^ (1 << 5))
            bt(index + 1)
        else:
            bt(index + 1)
    bt(0)
    return res



# 17. Letter Combinations of a Phone Number
'''
Runtime: 16 ms, faster than 89.24% of Python online submissions for Letter Combinations of a Phone Number.
Memory Usage: 11.9 MB, less than 12.47% of Python online submissions for Letter Combinations of a Phone Number.
'''
def letterCombinations(self, digits):
    if len(digits) == 0:
        return []
    dic, res = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}, []
    if len(digits) == 0: 
        return 0
    def bt(index, ans):
        if index == len(digits):
            res.append(ans)
            return
        for letter in dic[digits[index]]:
            bt(index+1, ans + letter)
    
    bt(0, '')
    return res
    
#  40. Combination Sum II
'''
Runtime: 32 ms, faster than 90.09% of Python online submissions for Combination Sum II.
Memory Usage: 11.7 MB, less than 78.40% of Python online submissions for Combination Sum II.
'''
def combinationSum2(self, candidates, target):
    res, num = [], sorted(candidates) + [0]
    def  df(index, total, ans):
        if index == len(num):
            return
        if total == target:
            res.append(ans)
            return
        if total + num[index] == target:
            res.append(ans + [num[index]])
            return
        else:
            for i in range(index, len(num)):
                if total + num[i] > target:
                    break
                if i > index and num[i] == num[i-1]:
                    continue
                df(i + 1, total + num[i], ans + [num[i]])
    df(0, 0, [])
    return res

# 46. Permutations
'''
Runtime: 24 ms, faster than 92.58% of Python online submissions for Permutations.
Memory Usage: 12 MB, less than 9.99% of Python online submissions for Permutations.
'''
def permute(self, nums):
    res = []
    def bt(visit, ans):
        if len(ans) == len(nums):
            res.append(ans)
            return
        for i in range(len(nums)):
            if nums[i] in visit:
                continue
            else:
                bt(visit + [nums[i]], ans + [nums[i]])
        return
    bt([], [])
    return res


# 47. Permutations II
'''
Runtime: 44 ms, faster than 77.14% of Python online submissions for Permutations II.
Memory Usage: 12.4 MB, less than 6.40% of Python online submissions for Permutations II.
'''

def permuteUnique(self, nums):
    res, nums = [], sorted(nums)
    def bt(nums, ans):
        if len(nums) == 0:
            res.append(ans)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            bt(nums[:i] + nums[i+1:], ans + [nums[i]])
    bt(nums, [])
    return res



# 52. N-Queens II
'''
Runtime: 76 ms, faster than 49.46% of Python online submissions for N-Queens II.
Memory Usage: 11.8 MB, less than 25.29% of Python online submissions for N-Queens II.
'''
def totalNQueens(self, n):
    """
    :type n: int
    :rtype: int
    """
    count = [0]
    
    def check(i, visit):
        if i in visit:
            return False
        for j in range(len(visit)):
            if visit[j] == i - len(visit) + j or visit[j] == i + len(visit) - j:
                return False
        return True

    def dfs(visit):
        if len(visit) == n:
            count[0] += 1
            return
        for i in range(0, n):
            if check(i, visit):
                dfs(visit + [i])
            else:
                continue
        return

    dfs([])
    return count[0]






















