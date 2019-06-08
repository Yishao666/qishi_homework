# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:12:09 2019

@author: Haoyi Lu
"""

'''
LC783

Runtime: 24 ms, faster than 45.57% of Python online submissions 
        for Minimum Distance Between BST Nodes.
Memory Usage: 11.8 MB, less than 79.40% of Python online submissions 
        for Minimum Distance Between BST Nodes.
'''

def minDiffInBST(self, root):
    self.small = -float('inf')
    self.res = float('inf')
    self.dfs(root)
    return self.res

def dfs(self, root):
    if root.left:
        self.dfs(root.left)
    self.res = min(self.res, root.val - self.small)
    self.small = root.val
    if root.right:
        self.dfs(root.right)

'''
LC 247

Runtime: 132 ms, faster than 48.43% of Python online submissions 
        for Strobogrammatic Number II.
Memory Usage: 17.5 MB, less than 26.90% of Python online submissions 
        for Strobogrammatic Number II.
'''
def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # head&tail: 00, 11, 69, 88, 96
        self.res = []
        self.dfs(n, '', '')
        return self.res
        
        
    def dfs(self, n, left, right):
        if n == 0:
            self.res.append(left + right)
            return
        elif n == 1:
            self.dfs(0, left + '0', right)
            self.dfs(0, left + '1', right)
            self.dfs(0, left + '8', right)
        else:
            if n != 2 and n != 3:
                self.dfs(n-2, '0' + left, right + '0' )
            self.dfs(n-2, '1' + left, right + '1' )
            self.dfs(n-2, '6' + left, right + '9' )
            self.dfs(n-2, '8' + left, right + '8' )
            self.dfs(n-2, '9' + left, right + '6' )

'''
LC 698

Runtime: 1804 ms, faster than 6.40% of Python online submissions 
        for Partition to K Equal Sum Subsets.
Memory Usage: 11.7 MB, less than 87.44% of Python online submissions 
        for Partition to K Equal Sum Subsets.

'''
    
def canPartitionKSubsets(self, nums, k):
    if sum(nums) % k != 0:
        return False
    else:
        parts = [sum(nums)/k] * k
        self.nums = sorted(nums, reverse=True)

    return self.dfs(0, parts)
    
def dfs(self, pos, parts):
    if pos == len(self.nums): return True
    
    for i,j in enumerate(parts):
        if self.nums[pos] <= j:
            parts[i] -= self.nums[pos]
            if self.dfs(pos+1, parts):
                return True
            parts[i] += self.nums[pos]
    return False
    
'''
LC544

Runtime: 32 ms, faster than 19.25% of Python online submissions 
        for Output Contest Matches.
Memory Usage: 12.3 MB, less than 25.40% of Python online submissions 
        for Output Contest Matches.
'''

def findContestMatch(self, n):
    rounds = int(math.log(n,2))
    schedule = [str(i) for i in range(1, n + 1)]
    while rounds > 0:
        n = 2**rounds
        rounds -= 1
        schedule = ['(' + schedule[i] + ','+ schedule[n - 1 - i] + ')' for i in range(2**rounds)]
    return schedule[0]
    