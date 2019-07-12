# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:10:47 2019

@author: Lu Haoyi
"""

# -----------------------Group A---------------------------------
'''
70. Climbing Stairs

Runtime: 16 ms, faster than 79.75% of Python online submissions for Climbing Stairs.
Memory Usage: 11.6 MB, less than 85.59% of Python online submissions for Climbing Stairs.
'''
def climbStairs(self, n):
    if n == 0:  return 0
    if n == 1:  return 1
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


'''
53. Maximum Subarray

Runtime: 52 ms, faster than 72.68% of Python online submissions for Maximum Subarray.
Memory Usage: 12.4 MB, less than 35.67% of Python online submissions for Maximum Subarray.
'''
def maxSubArray(self, nums):
    if len(nums) == 0:
        return 0
    dp, res = nums[0], nums[0]
    for i in range(1, len(nums)):
        dp = max(dp + nums[i], nums[i])
        if dp > res:
            res = dp
    return res
        

'''
647. Palindromic Substrings

Runtime: 320 ms, faster than 30.05% of Python online submissions for Palindromic Substrings.
Memory Usage: 19.5 MB, less than 20.68% of Python online submissions for Palindromic Substrings.
'''
def countSubstrings(self, s):
    if not s:
        return 0
    dp = [[0] * len(s) for i in range(len(s))]
    count = 0
    for j in range(len(s)):
        for i in range(j+1):
            if i == j:
                dp[i][j] = 1
            elif j - i == 1:
                dp[i][j] = 1 if s[i] == s[j] else 0
            else:
                dp[i][j] = 1 if dp[i+1][j-1] == 1 and s[i] == s[j] else 0
            if dp[i][j] == 1:
                count += 1
    return count


'''
486. Predict the Winner

Runtime: 20 ms, faster than 80.79% of Python online submissions for Predict the Winner.
Memory Usage: 11.9 MB, less than 27.55% of Python online submissions for Predict the Winner.
'''
def PredictTheWinner(self, nums):
    # 我的思路，dp[i][j]代表先手面对nums[i:j]的局面最多拿的分数
    dp = [[0] * len(nums) for i in range(len(nums))]
    
    for j in range(len(nums)):
        for i in range(j, -1, -1):
            if i == j:
                dp[i][j] = nums[i]
            elif j - i == 1:
                dp[i][j] = max(nums[i], nums[j])
            else:
                dp[i][j] = sum(nums[i:j+1]) - min(dp[i+1][j], dp[i][j-1])
    if dp[0][len(nums) - 1] >= sum(nums) - dp[0][len(nums) - 1]:
        return True
    else:
        return False

#------------------------Group A optional------------------------------
        
'''
64. Minimum Path Sum

Runtime: 80 ms, faster than 83.12% of Python online submissions for Minimum Path Sum.
Memory Usage: 12.4 MB, less than 88.58% of Python online submissions for Minimum Path Sum.
'''
def minPathSum(self, grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    m, n = len(grid), len(grid[0])
    dp1, dp2 = [grid[0][0]]*n, [0]*n
    for i in range(1, n):
        dp1[i] = dp1[i-1] + grid[0][i]
    
    for i in range(1, m):
        if i % 2 == 1:
            dp2[0] = dp1[0] + grid[i][0]
            for j in range(1, n):
                dp2[j] = min(dp2[j-1], dp1[j]) + grid[i][j]
        else:
            dp1[0] = dp2[0] + grid[i][0]
            for j in range(1, n):
                dp1[j] = min (dp1[j-1], dp2[j]) + grid[i][j]
    return dp1[-1] if m%2 == 1 else dp2[-1]


'''
718. Maximum Length of Repeated Subarray

Runtime: 3660 ms, faster than 42.80% of Python online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 32.9 MB, less than 52.92% of Python online submissions for Maximum Length of Repeated Subarray.
'''
def findLength(self, A, B):
    if not A or not B:
        return 0
    dp = [[0] * len(A) for i in range(len(B))]
    res = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if i == 0 or j == 0:
                dp[i][j] = 1 if A[i] == B[j] else 0
            else:
                dp[i][j] = dp[i-1][j-1] + 1 if A[i] == B[j] else 0
            if dp[i][j] > res:
                res = dp[i][j]
    return res
























